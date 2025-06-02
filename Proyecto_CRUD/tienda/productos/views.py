from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/producto_list.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion', 'imagen']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def post(self, request, *args, **kwargs):
        request.FILES.get('imagen')
        return super().post(request, *args, **kwargs)

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'descripcion', 'imagen']
    template_name = 'productos/producto_form.html'
    success_url = reverse_lazy('producto_list')

    def post(self, request, *args, **kwargs):
        request.FILES.get('imagen')
        return super().post(request, *args, **kwargs)

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')
