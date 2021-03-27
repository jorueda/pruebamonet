from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .models import Control, Detalle
from monet.serializers import ControlSerializer, DetalleSerializer


class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
    permission_classes = [permissions.IsAuthenticated]


class DetalleViewSet(viewsets.ModelViewSet):
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer
    permission_classes = [permissions.IsAuthenticated]
