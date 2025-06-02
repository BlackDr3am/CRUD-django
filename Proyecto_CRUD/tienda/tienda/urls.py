from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from productos.views import ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView

urlpatterns = [
    path('', ProductoListView.as_view(), name='producto_list'),
    path('crear/', ProductoCreateView.as_view(), name='producto_create'),
    path('editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
]

# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
