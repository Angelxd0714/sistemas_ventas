import os
from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    dni = models.IntegerField(unique=True, null=False, blank=False,verbose_name="dni")
    nombres= models.CharField(max_length=50, null=False, blank=False, verbose_name="nombres")
    apellidos = models.CharField(max_length=50, null=False, blank=False, verbose_name="apellidos")
    fecha_nac = models.DateField(null=False, blank=False, verbose_name="fecha_nac")
    direccion = models.CharField(max_length=50, null=False, blank=False, verbose_name="direccion")
    imagen_usuario = models.ImageField(default=None,null=False, blank=False, verbose_name="imagen_usuario", upload_to="user_imagen/")
    sexo = models.CharField(max_length=1, null=False, blank=False, verbose_name="sexo")
    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id_cliente']
        unique_together = ('dni',)
        # app_label = 'app_name'
        # db_tablespace = 'tablespace_name'
        # default_permissions = ()
        # permissions = ()
        indexes = [
            models.Index(fields=['dni']),
        ]
        # constraints = ()
        # proxy = False
        # swappable = 'app_label.ModelName'
        # index_together = ()
        # base_manager_name = 'objects'
        # default_manager_name = 'objects'
        # abstract = False
        # managed = True
        # proxy_for_model = None
        # verbose_name = 'verbose_name'
        # verbose_name_plural = 'verbose_name_plural'
        # help_text = 'help_text'
        # app_config = None
        # db_table = 'table_name'
        # managed = True
        # unique_together = ()
    def __str__(self):
        return self.dni + '|' + self.nombres + '|' + self.apellidos + '|' + self.fecha_nac + '|' + self.direccion + '|' + self.sexo + '|' + str(self.id_cliente)
    def toJson(self):
        return {
            'id_cliente': self.id_cliente,
            'dni': self.dni,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'fecha_nac': self.fecha_nac,
            'direccion': self.direccion,
            'imagen_usuario': self.imagen_usuario.url if self.imagen_usuario else None,
            'sexo': self.sexo
        }
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, null=False, blank=False, verbose_name="nombre_categoria")
    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id_categoria']
        
        # app_label = 'app_name'
        # db_tablespace = 'tablespace_name'
        # default_permissions = ()
        # permissions = ()
        indexes = [
            models.Index(fields=['nombre_categoria']),
        ]
        # constraints = ()
        # proxy = False
        # swappable = 'app_label.ModelName'
        # index_together = ()
        # base_manager_name = 'objects'
        # default_manager_name = 'objects'
        # abstract = False
        # managed = True
        # proxy_for_model = None
        # verbose_name = 'verbose_name'
        # verbose_name_plural = 'verbose_name_plural'
        # help_text = 'help_text'
        # app_config = None
        # db_table = 'table_name'
    def __str__(self):
        return self.nombre_categoria + '|' + str(self.id_categoria)
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50, null=False, blank=False, verbose_name="nombre_producto")
    precio_producto = models.IntegerField(null=False, blank=False, verbose_name="precio_producto")
    stock = models.IntegerField(null=False, blank=False, verbose_name="stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    pvp = models.IntegerField(null=False, blank=False, verbose_name="pvp")
    class Meta:
        db_table = 'producto'

        verbose_name = 'Producto'

        verbose_name_plural = 'Productos'
        ordering = ['id_producto']
        unique_together = ('nombre_producto',)

        # app_label = 'app_name'
        # db_tablespace = 'tablespace_name'
        # default_permissions = ()
        indexes = [
            models.Index(fields=['nombre_producto']),
        ]
    def __str__(self):
        return self.nombre_producto + '|' + str(self.precio_producto) + '|' + str(self.stock) + '|' + str(self.categoria) + '|' + str(self.pvp)

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_venta = models.DateField(null=False, blank=False, verbose_name="fecha_venta")
    subtotal = models.DecimalField(max_digits=5, decimal_places=2,null=False, blank=False, verbose_name="subtotal")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    iva= models.DecimalField(max_digits=5, decimal_places=2,null=False, blank=False, verbose_name="iva")
    total = models.DecimalField(max_digits=5, decimal_places=2,null=False, blank=False, verbose_name="total")
    class Meta:
        db_table ='ventas'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id_venta']
        unique_together = ('fecha_venta',)
        # app_label = 'app_name'
        # db_tablespace = 'tablespace_name'
        # default_permissions = ()
        indexes = [
            models.Index(fields=['fecha_venta']),
        ]
    def __str__(self):
        return self.fecha_venta + '|' + str(self.subtotal) + '|' + str(self.iva) + '|' + str(self.total)
class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, blank=False, verbose_name="cantidad")
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="precio")
    subtotal = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, verbose_name="subtotal")
    class Meta:
        db_table = 'detalle_venta'
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        ordering = ['id_detalle_venta']
        unique_together = ('producto',)
        # app_label = 'app_name'
        # db_tablespace = 'tablespace_name'
        # default_permissions = ()
        indexes =[
            models.Index(fields=['producto']),
        ]

    def __str__(self):
        return self.producto.nombre_producto + ' ' + str(self.cantidad) + ' ' + str(self.precio) + ' ' + str(self.subtotal)
    