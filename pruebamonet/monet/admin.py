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

admin.site.register(Control, ControlAdmin)
admin.site.register(Archivo)
