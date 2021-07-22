from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from AdministrApp.models import cliente, inmueble, instalacion, solicitud, estado
from AdministrApp.models import aporte, gastoOperativo, estadoInstalacion, plan, material
from AdministrApp.models import planInstalacion, pagoServicio, materialInstalacion

# Register your models here.

class estadoInstalacionInLine(admin.TabularInline):
    model=estadoInstalacion
    extra=1
    

class planInstalacionInLine(admin.TabularInline):
    model=planInstalacion
    extra=1

class materialInstalacionInLine(admin.TabularInline):
    model=materialInstalacion
    extra=2

class instalacionAdmin(admin.ModelAdmin):
    inlines=[estadoInstalacionInLine, planInstalacionInLine, materialInstalacionInLine,]
    list_display=('id', 'fecha_instalacion', 'nad_instalacion', 'ip_instalacion', 'valor_instalacion','id_cliente', 'id_inmueble', 'obs_instalacion')
    list_filter=('id_cliente',)

class clienteAdmin(admin.ModelAdmin):
    list_display=('fecha_cliente', 'perfil_cliente', 'documento_cliente', 'nombre_cliente', 'apellido_cliente', 'celular_cliente', 'correo_cliente', 'genero_cliente')
    list_filter=('perfil_cliente', 'apellido_cliente',)

class inmuebleAdmin(admin.ModelAdmin):
    list_display=('gps_inmueble', 'direccion_inmueble', 'barrio_inmueble', 'ciudad_inmueble')
    list_filter=('barrio_inmueble',)
    
class solicitudAdmin(admin.ModelAdmin):
    list_display=('tipo_solicitud', 'fechaInicia_solicitud', 'obsInicia_solicitud', 'fechaFinal_solicitud', 'obsFinal_solicitud', 'estado_solicitud', 'id_instalacion')

class aporteAdmin(admin.ModelAdmin):
    list_display=('fecha_aporte', 'valor_aporte', 'obs_aporte', 'id_cliente')
    list_filter=('id_cliente', 'fecha_aporte')

class gastoOperativoAdmin(admin.ModelAdmin):
    list_display=('concepto_gastoOperativo', 'fecha_gastoOperativo', 'obs_gastoOperativo', 'id_cliente')

class estadoInstalacionAdmin(admin.ModelAdmin):
    list_display=('fecha_estadoInstalacion', 'obs_estadoInstalacion')

class estadoAdmin(admin.ModelAdmin):
    list_display=('nombre_estado',)

class planAdmin(admin.ModelAdmin):
    list_display=('fecha_plan', 'nombre_plan', 'valor_plan', 'estado_plan')

class planInstalacionAdmin(admin.ModelAdmin):
    list_display=('fecha_planInstalacion', 'id_plan', 'id_instalacion')

class pagoServicioAdmin(admin.ModelAdmin):
    list_display=('fecha_pagoServicio', 'valor_pagoServicio', 'obs_pagoServicio', 'id_instalacion')

class materialInstalacionAdmin(admin.ModelAdmin):
    list_display=('fecha_materialInstalacion', 'obs_materialInstalacion', 'id_material', 'id_instalacion')

class materialAdmin(admin.ModelAdmin):
    list_display=('fecha_material', 'nombre_material', 'mac_material', 'userPass_material', 'estado_material' ,'obs_material')



admin.site.register(cliente, clienteAdmin)
admin.site.register(inmueble, inmuebleAdmin)
admin.site.register(instalacion, instalacionAdmin)
admin.site.register(solicitud, solicitudAdmin)
admin.site.register(aporte, aporteAdmin)
admin.site.register(gastoOperativo, gastoOperativoAdmin)
admin.site.register(estadoInstalacion,estadoInstalacionAdmin)
admin.site.register(estado, estadoAdmin)
admin.site.register(plan, planAdmin)
#admin.site.register(planInstalacion,planInstalacionAdmin)
admin.site.register(pagoServicio, pagoServicioAdmin)
#admin.site.register(materialInstalacion, materialInstalacionAdmin)
admin.site.register(material, materialAdmin)