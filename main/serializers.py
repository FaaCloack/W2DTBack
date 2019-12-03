from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Lugar, Categoria, Precio, Resenas


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class LugarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        precio = serializers.PrimaryKeyRelatedField(
            queryset=Precio.objects.all(),
            many=False)
        categoria = serializers.PrimaryKeyRelatedField(
            queryset=Categoria.objects.all(),
            many=False)
        model = Lugar
        fields = ['nombre', 'direccion', 'latitud', 'longitud', 'categoria', 'precio']


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class PrecioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'


class ResenasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resenas
        fields = '__all__'
