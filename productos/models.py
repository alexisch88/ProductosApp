from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()
    imagen = models.ImageField(upload_to='productos')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
