from django.contrib import admin

# Register your models here.
from .models import Detalle, Control

class DetalleInLine(admin.TabularInline):
    model = Detalle
    extra = 3


class ControlAdmin(admin.ModelAdmin):
    inlines = [DetalleInLine]


admin.site.register(Control, ControlAdmin)
