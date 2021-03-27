from django.db import models

# Create your models here.


class Control(models.Model):
    tipo_registro = models.PositiveSmallIntegerField(default = 0) # Longitud 1
    nit_entidad = models.PositiveBigIntegerField(default = 0) # Longitud 13
    nombre_recaudadora = models.CharField(max_length = 20, default = "", blank = True)
    codigo_convenio = models.PositiveBigIntegerField(default = 0) # Longitud 15
    fecha_transmision = models.PositiveIntegerField(default = 0) # Longitud 8
    secuencia_envio = models.CharField(max_length = 1, default = "")
    fecha_vencimiento = models.PositiveIntegerField(default = 0) # Longitud 8
    numero_registros = models.PositiveIntegerField(default = 0) # Longitud 8
    valor_total_transacciones = models.PositiveBigIntegerField(default = 0) # Longitud 17
    reservado = models.CharField(max_length = 79, default = "", blank = True)

    def __str__(self):
        return '%s %s' % (self.nit_entidad, self.fecha_transmision)


class Detalle(models.Model):
    tipo_registro = models.PositiveSmallIntegerField() # Longitud 1
    nit_pagador = models.CharField(max_length = 13, blank = True)
    nombre_pagador = models.CharField(max_length = 20, blank = True)
    cuenta_pagador = models.CharField(max_length = 9, blank = True)
    cuenta_debitar = models.CharField(max_length = 17, blank = True)
    tipo_transaccion = models.CharField(max_length = 2, blank = True)
    valor_transaccion = models.PositiveBigIntegerField() # Longitud 17
    indicador_validacion = models.CharField(max_length = 1, blank = True)
    referencia_1 = models.CharField(max_length = 30, blank = True)
    referencia_2 = models.CharField(max_length = 30, blank = True)
    fecha_vencimiento = models.PositiveIntegerField(blank = True) # Longitud 8
    periodos_facturados = models.CharField(max_length = 2, blank = True)
    ciclo = models.CharField(max_length = 3, blank = True)
    reservado = models.CharField(max_length = 17, blank = True)
    control = models.ForeignKey('monet.Control', on_delete = models.CASCADE, default = "")


class Archivo(models.Model):
    archivo_texto = models.FileField(default = "")

    def __str__(self):
        return self.archivo_texto
