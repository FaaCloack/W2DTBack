from django.contrib.auth.models import User, Group
from main.models import Lugar, Categoria, Precio, Resenas
from rest_framework import viewsets
from main.serializers import ResenasSerializer, UserSerializer, GroupSerializer, LugarSerializer, CategoriaSerializer, PrecioSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LugarViewSet(APIView):
    # queryset = Lugar.objects.all()
    serializer_class = LugarSerializer

    def get(self, request, format=None):
        lugares = Lugar.objects.all()
        serializer = LugarSerializer(lugares, many=True, context={'request': request})
        return Response({'message': 'Sucess',
                         'lugares': serializer.data}, status=200)

    def post(self, request):
        action = request.POST.get('action')
        if(action == 'registrar'):
            categoria = Categoria.objects.get(nombre=request.POST.get('categoria'))
            precio = Precio.objects.get(nombre=request.POST.get('precio'))
            lugar = Lugar()
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            latitud = request.POST.get('latitud')
            longitud = request.POST.get('longitud')

            lugar.nombre = nombre
            lugar.direccion = direccion
            lugar.latitud = latitud
            lugar.longitud = longitud
            lugar.categoria = categoria
            lugar.precio = precio
            lugar.save()

            return Response({'data': 'SUCCESS'},
                            content_type="application/json", status=200)
        elif(action == 'eliminar'):
            lugar = Lugar.objects.filter(nombre=request.POST.get('nombre'))
            lugar.delete()
            return Response({'data': 'SUCCESS'},
                            content_type="application/json", status=200)
        else:
            lugar = Lugar.objects.get(nombre=request.POST.get('key'))
            nombre = request.POST.get('nombre')
            direccion = request.POST.get('direccion')
            latitud = request.POST.get('latitud')
            longitud = request.POST.get('longitud')

            lugar.nombre = nombre
            lugar.direccion = direccion
            lugar.latitud = latitud
            lugar.longitud = longitud
            lugar.save()

            print(nombre)

            return Response({'data': 'SUCCESS'},
                            content_type="application/json", status=200)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PrecioViewSet(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer


class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resenas.objects.all()
    serializer_class = ResenasSerializer
