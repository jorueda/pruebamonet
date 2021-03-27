from .models import Control, Detalle
from rest_framework import serializers


class ControlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'


class DetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detalle
        fields = '__all__'
