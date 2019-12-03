from django.contrib.auth.models import User, Group
from rest_framework import serializers
from main.models import Lugar, Categoria, Precio


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
        model = Lugar
        fields = '__all__'


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class PrecioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Precio
        fields = '__all__'
