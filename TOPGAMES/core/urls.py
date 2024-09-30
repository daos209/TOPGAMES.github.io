from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, login, carrito, modificar_perfil
from django.urls import path
from .views import PayPalExecuteAPIView, pago_exitoso
from django.urls import path
from .views import PayPalExecuteAPIView, pago_exitoso, CustomTokenObtainPairView

urlpatterns = [
    path('api/paypal/execute/', PayPalExecuteAPIView.as_view(), name='paypal-execute'),
    path('pago-exitoso/', pago_exitoso, name='pago-exitoso'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # core/urls.py
    # Ruta para ejecutar el pago
    path('api/paypal/execute/', PayPalExecuteAPIView.as_view(), name='paypal-execute'),
    # Ruta para mostrar el mensaje de éxito
    path('pago-exitoso/', pago_exitoso, name='pago-exitoso'),
    # Ruta principal que renderiza la vista del índice
    path('', index, name='core/index'),

    # Ruta para la página de inicio de sesión
    path('login/', login, name='core/login'),

    # Ruta para el carrito de compras
    path('carrito/', carrito, name='core/carrito'),

    # Ruta para modificar el perfil del usuario
    path('modificar_perfil/', modificar_perfil, name='core/modificar_perfil'),
    
    # Rutas para la recuperación de contraseña
    path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='core/password_reset.html'), 
         name='password_reset'),
    
    path('password_reset_done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), 
         name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), 
         name='password_reset_confirm'),
    
    path('password_reset_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), 
         name='password_reset_complete'),
]

