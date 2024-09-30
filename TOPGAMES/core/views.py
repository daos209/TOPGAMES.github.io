# core/views.py
import paypalrestsdk
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class PayPalExecuteAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder a esta vista

    def post(self, request, *args, **kwargs):
        payment_id = request.data.get("paymentID")
        payer_id = request.data.get("payerID")

        payment = paypalrestsdk.Payment.find(payment_id)

        if payment:
            if payment.execute({"payer_id": payer_id}):
                return JsonResponse({"message": "Pago completado con éxito"}, status=200)
            else:
                return JsonResponse({"error": payment.error}, status=400)
        else:
            return JsonResponse({"error": "Pago no encontrado"}, status=404)
# No es necesario agregar código adicional, simplemente importa la vista
class CustomTokenObtainPairView(TokenObtainPairView):
    # Aquí puedes personalizar la respuesta si es necesario
    pass

# Configura PayPal
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,  # 'sandbox' o 'live'
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

class PayPalPaymentAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener el monto del pago del request (se puede personalizar según lo que envíe el frontend)
        amount = request.data.get("amount", "20.00")  # Valor predeterminado si no se proporciona

        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://localhost:8000/api/paypal/execute/",  # Cambiar en producción
                "cancel_url": "http://localhost:8000/cancel/"  # Cambiar en producción
            },
            "transactions": [{
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": "Compra en TopGames"
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    return JsonResponse({"approval_url": link.href})
        else:
            return JsonResponse({"error": payment.error}, status=400)
