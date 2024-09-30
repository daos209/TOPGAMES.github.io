from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# core/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import PagoSerializer

class PagoAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            # Aquí se puede añadir la lógica para procesar el pago, como la integración con un gateway de pagos
            # Por ejemplo, podrías enviar los detalles a una API de pagos como Stripe, PayPal, etc.
            return Response({'mensaje': 'Pago procesado correctamente.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    return render(request, 'core/login.html')

def carrito(request):
    return render(request, 'core/carrito.html')

@login_required
def modificar_perfil(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        user = request.user
        user.username = username

        if password and password == confirm_password:
            user.set_password(password)
            update_session_auth_hash(request, user) 

        user.save()
        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('modificar_perfil')

    return render(request, 'core/moduser.html', {'user': request.user})
