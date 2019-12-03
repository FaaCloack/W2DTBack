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
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    latitud = models.CharField(max_length=30)
    longitud = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.ForeignKey(Precio, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class Resenas(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    lugar = models.CharField(max_length=30)
    texto = models.CharField(max_length=200)

    def __unicode__(self):
        return self.id
