from django.contrib.auth.views import LoginView
from django.urls import path
from productos.views import (
    RegistroUsuarioView, LoginUsuarioView, LogoutUsuarioView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView,
    ImagenProductoCreateView, FinalizarCompraView
)

urlpatterns = [
     path('accounts/login/', LoginView.as_view(), name='login'),  # Agregar esta ruta
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('login/', LoginUsuarioView.as_view(), name='login_usuario'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout_usuario'),
    path('', ProductoListView.as_view(), name='producto_list'),
    path('producto/agregar/', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
    path('producto/imagen/agregar/', ImagenProductoCreateView.as_view(), name='agregar_imagen'),
    path('compra/finalizar/', FinalizarCompraView.as_view(), name='finalizar_compra'),
]
