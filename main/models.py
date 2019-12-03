from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Precio(models.Model):
    nombre = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nombre


class Lugar(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    url = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre
