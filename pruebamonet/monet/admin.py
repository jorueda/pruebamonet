from django.contrib import admin

# Register your models here.
from .models import Detalle, Control, Archivo

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 1


class ControlAdmin(admin.ModelAdmin):
    inlines = [DetalleInLine]
    list_display = ('nit_entidad', 'fecha_transmision', 'numero_registros', 'valor_total_transacciones')
    list_filter = ('nit_entidad', 'fecha_transmision', 'numero_registros', 'valor_total_transacciones')
    search_fields = ('nit_entidad', 'fecha_transmision', 'valor_total_transacciones')


class ArchivoAdmin(admin.ModelAdmin):
    model = Archivo

    def save_model(self, request, obj, form, change):
        lista_control = [1, 13, 20, 15, 8, 1, 8, 8, 17, 79]
        lista_detalle = [1, 13, 20, 9, 17, 2, 17, 1, 30, 30, 8, 2, 3, 17]

        objeto = str(obj.archivo_texto.readline())
        objeto = objeto[1:]
        start = 1
        lista_objeto = []
        for chunk in lista_control:
            lista_objeto.append(objeto[start:start+chunk])
            start = start + chunk

        nuevo_control = Control.objects.create(
            tipo_registro = lista_objeto[0],
            nit_entidad = lista_objeto[1],
            nombre_recaudadora = lista_objeto[2],
            codigo_convenio = lista_objeto[3],
            fecha_transmision = lista_objeto[4],
            secuencia_envio = lista_objeto[5],
            fecha_vencimiento = lista_objeto[6],
            numero_registros = lista_objeto[7],
            valor_total_transacciones = lista_objeto[8],
            reservado = lista_objeto[9],
            )

        nuevo_control.save()

        objeto = str(obj.archivo_texto.readline())
        while len(objeto) > 3:
            objeto = objeto[1:]
            start = 1
            lista_objeto = []
            for chunk in lista_detalle:
                lista_objeto.append(objeto[start:start+chunk])
                start = start + chunk
            nuevo_detalle = Detalle.objects.create(
                tipo_registro = lista_objeto[0],
                nit_pagador = lista_objeto[1],
                nombre_pagador = lista_objeto[2],
                cuenta_pagador = lista_objeto[3],
                cuenta_debitar = lista_objeto[4],
                tipo_transaccion = lista_objeto[5],
                valor_transaccion = lista_objeto[6],
                indicador_validacion = lista_objeto[7],
                referencia_1 = lista_objeto[8],
                referencia_2 = lista_objeto[9],
                fecha_vencimiento = lista_objeto[10],
                periodos_facturados = lista_objeto[11],
                ciclo = lista_objeto[12],
                reservado = lista_objeto[13],
                control = nuevo_control,
                )
            nuevo_detalle.save()
            objeto = str(obj.archivo_texto.readline())

        obj.save()

admin.site.register(Control, ControlAdmin)
admin.site.register(Archivo, ArchivoAdmin)
