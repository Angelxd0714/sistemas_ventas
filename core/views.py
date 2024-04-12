from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from core.models import *
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your views here.
def home(request):
    data = {

        'title': 'pagina1',
    }
    return render(request,'index.html',data)



class CategoriaView(ListView):
    model = Categoria
    template_name = 'categoria.html'
    context_object_name = 'categorias'  # Nombre con el que se accederá a la lista de categorías en la plantilla
    success_url = reverse_lazy('categoria_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Obtener todos los objetos de Categoria
        return context
    def post(self, request, *args, **kwargs):
        nombre_categoria = request.POST.get('nombre_categoria')
        categoria = Categoria(nombre_categoria=nombre_categoria)
        
        categoria.save()
        return HttpResponseRedirect(self.success_url)
    
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoriaCreate.html'
    fields = ['nombre_categoria']
    success_url = reverse_lazy('categoria_list') 
    def post(self, request, *args, **kwargs):
        nombre_categoria = request.POST.get('nombre_categoria')
        categoria = Categoria(nombre_categoria=nombre_categoria)
        categoria.save()
        return HttpResponseRedirect(self.success_url)

class CategeriaUpdate(UpdateView):
    model = Categoria
    template_name = 'modalCategoria.html'
    fields = ['nombre_categoria']
    success_url = reverse_lazy('categoria_list') 

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'categoria.html'
    success_url = reverse_lazy('categoria_list')
    def delete(self, request, *args, **kwargs):
        # Obtiene el objeto de categoría
        self.object = self.get_object()
        # Elimina la categoría
        self.object.delete()
        # Retorna una respuesta JSON indicando que la categoría fue eliminada exitosamente
        return JsonResponse({'message': 'Categoría eliminada exitosamente.'})


class ProductoView(CreateView):
    model = Producto
    template_name = 'Productos.html'
    fields = ['nombre_producto','precio_producto','categoria']
    success_url = reverse_lazy('producto_list')
    def post(self, request, *args, **kwargs):
        if request is None:
            return JsonResponse({'error': 'No se ha proporcionado una solicitud.'})
        nombre_producto = request.POST.get('nombre_producto')
        precio_producto = request.POST.get('precio_producto')
        categoria = request.POST.get('categoria')
        stock = request.POST.get('stock')
        pvp = request.POST.get('pvp')
        imagen_producto = request.FILES.get('imagen_producto')  # Obtener el archivo de imagen desde la solicitud
        
        # Crear una instancia de SimpleUploadedFile para el archivo de imagen
        if imagen_producto:
            archivo_imagen = SimpleUploadedFile(imagen_producto.name, imagen_producto.read(), content_type=imagen_producto.content_type)
        else:
            archivo_imagen = None
            return JsonResponse({'error': 'No se ha proporcionado una imagen.'})
        
        producto = Producto(nombre_producto=nombre_producto, precio_producto=precio_producto,stock=stock ,categoria=categoria, imagen_producto=archivo_imagen,pvp=pvp)
        producto.save()
        
        return JsonResponse(producto)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Obtener todas las categorías
        return context
    