# core/serializers.py
from rest_framework import serializers

class PagoSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    metodo_pago = serializers.ChoiceField(choices=[('tarjeta', 'Tarjeta de Crédito/Débito'), ('paypal', 'PayPal'), ('transferencia', 'Transferencia Bancaria')])
    numero_tarjeta = serializers.CharField(max_length=16, required=False, allow_blank=True)
    fecha_expiracion = serializers.CharField(max_length=5, required=False, allow_blank=True)
    cvv = serializers.CharField(max_length=3, required=False, allow_blank=True)

    def validate(self, data):
        # Validación personalizada para campos obligatorios según el método de pago
        if data['metodo_pago'] == 'tarjeta':
            if not data['numero_tarjeta'] or not data['fecha_expiracion'] or not data['cvv']:
                raise serializers.ValidationError("Todos los campos de la tarjeta son obligatorios.")
        return data
