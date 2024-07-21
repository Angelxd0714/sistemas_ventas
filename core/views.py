from django.conf import settings
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
        imagen_producto = request.FILES.get('imagen_producto') 
         # Obtener el archivo de imagen desde la solicitud
       
        categoria = Categoria.objects.get(id_categoria=categoria)
        # Crear una instancia de SimpleUploadedFile para el archivo de imagen
        if imagen_producto:
            
            archivo_imagen = SimpleUploadedFile(imagen_producto.name, imagen_producto.read(), content_type=imagen_producto.content_type)
            
        else:
            archivo_imagen = None
            return JsonResponse({'error': 'No se ha proporcionado una imagen.'})
        
        producto = Producto(nombre_producto=nombre_producto, precio_producto=precio_producto,stock=stock ,categoria=categoria, imagen=archivo_imagen,pvp=pvp)
        producto.save()
        
        return JsonResponse({"status": "success"})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()  # Obtener todas las categorías
        return context
    
class ProductoListView(ListView):
    model = Producto
    template_name = 'ProductosAll.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
         # Obtener todos los productos
        return context
    
class ClientesListView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context
    def post(self,request, *args, **kwargs):
        listar_clientes=[]

        try:
            action = request.POST.get("action")
            if action == "searchdata":
                clientes = Cliente.objects.all()
                for cliente in clientes:
                    listar_clientes.append(cliente.toJson())
            return JsonResponse(data=listar_clientes, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)})
class CLientesCreate(CreateView):
    model = Cliente
    template_name = 'clientes.html'
    fields = ['dni','nombres','apellidos','fecha_nac','direccion','imagen_usuario','sexo']
    
    def post(self, request, *args, **kwargs):
        print(request.POST.get("imagen_usuario"))
        try:
            action = request.POST.get('action')
            if action == 'create':
                dni = request.POST.get('dni')
                nombres = request.POST.get('nombres')
                apellidos = request.POST.get('apellidos')
                fecha_nac = request.POST.get('fecha_nac')
                direccion = request.POST.get('direccion')
                imagen_usuario = request.FILES.get('imagen_usuario')
                sexo = request.POST.get('sexo')
                cliente = Cliente(dni=dni, nombres=nombres, apellidos=apellidos, fecha_nac=fecha_nac, direccion=direccion, imagen_usuario=imagen_usuario, sexo=sexo)
                cliente.save()
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({'error': 'Invalid action'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
           