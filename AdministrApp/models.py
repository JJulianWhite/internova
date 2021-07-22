#from _typeshed import Self
from typing import Iterable
from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from .choices import genero, perfil, barrio, ciudad, tipoSolicitud, estadoSolicitud, operativos


# Create your models here.


#--CLIENTE--
class cliente(models.Model):
    fecha_cliente=models.DateField(auto_now=True, verbose_name="Fecha")
    documento_cliente=models.CharField(max_length=20, verbose_name='Número de Documento')
    nombre_cliente=models.CharField(max_length=100, verbose_name='Nombre')
    apellido_cliente=models.CharField(max_length=100, verbose_name='Apellido')
    celular_cliente=models.CharField(max_length=20, verbose_name='Número Celular')
    correo_cliente=models.EmailField(max_length=100, verbose_name='Correo Electónico')
    genero_cliente=models.CharField(max_length=20, choices=genero, verbose_name='Género', default=0)
    perfil_cliente=models.CharField(max_length=20, choices=perfil, verbose_name='Perfil', default=0)
    obs_cliente=models.TextField(verbose_name='Observación', null=True, blank=True)

    def __str__(self) -> str:
        return self.apellido_cliente + ' ' + self.nombre_cliente

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['apellido_cliente']


#--INMUEBLE--
class inmueble(models.Model):
    gps_inmueble=models.CharField(max_length=20, verbose_name='Punto GPS')
    direccion_inmueble=CharField(max_length=100, verbose_name='Dirección')
    barrio_inmueble=CharField(max_length=20, verbose_name='Barrio', choices=barrio, default=0)
    ciudad_inmueble=CharField(max_length=20, verbose_name='Ciudad', choices=ciudad, default=0)

    def __str__(self) -> str:
        return self.direccion_inmueble + ' - ' + self.barrio_inmueble

    class Meta:
        verbose_name='Inmueble'
        verbose_name_plural='Inmuebles'
        ordering=['barrio_inmueble', 'direccion_inmueble',]


#--APORTE--
class aporte(models.Model):
    fecha_aporte=models.DateField(verbose_name='Fecha')
    valor_aporte=models.IntegerField(verbose_name='Valor')
    obs_aporte=models.TextField(verbose_name='Observación')
    id_cliente=models.ForeignKey(cliente, verbose_name='Nombre Socio', on_delete=models.CASCADE)

    class Meta:
        verbose_name='Aporte'
        verbose_name_plural='Aportes'
        ordering=['id_cliente', 'valor_aporte',]


#--GASTO OPERATIVO--
class gastoOperativo(models.Model):
    fecha_gastoOperativo=models.DateField(verbose_name='Fecha')
    concepto_gastoOperativo=models.CharField(max_length=20, verbose_name='Concepto', choices=operativos, default=0)
    obs_gastoOperativo=models.TextField(verbose_name='Observacion')
    id_cliente=models.ForeignKey(cliente, verbose_name='Cliente', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name='Gasto Operativo'
        verbose_name_plural='Gastos Operativos'
        ordering=['id_cliente', 'concepto_gastoOperativo',]


#--ESTADO--
class estado(models.Model):
    nombre_estado=models.CharField(max_length=20, verbose_name='Estado', choices=estadoSolicitud)

    def __str__(self) -> str:
        return self.nombre_estado

    class Meta:
        verbose_name='Estado'
        verbose_name_plural='Estados'
        ordering=['nombre_estado',]


#--PLAN--
class plan(models.Model):
    fecha_plan=models.DateField(verbose_name='Fecha')
    nombre_plan=models.CharField(max_length=100, verbose_name='Nombre Plan')
    valor_plan=models.IntegerField(verbose_name='Valor Plan')
    estado_plan=models.CharField(max_length=20, choices=estadoSolicitud)
    
    def __str__(self) -> str:
        return self.nombre_plan

    class Meta:
        verbose_name='Plan'
        verbose_name_plural='Planes'
        ordering=['fecha_plan',]


#--MATERIAL--
class material(models.Model):
    fecha_material=models.DateField(verbose_name='Fecha')
    nombre_material=models.CharField(max_length=100, verbose_name='Nombre Material')
    mac_material=models.CharField(max_length=100, verbose_name='MAC-Referencia')
    userPass_material=models.CharField(max_length=100, verbose_name='User / Pass', null=True, blank=True)
    obs_material=models.TextField(verbose_name='Observación')
    estado_material=models.CharField(max_length=20, verbose_name='Estado', choices=estadoSolicitud, default=0)

    def __str__(self) -> str:
        return self.nombre_material

    class Meta:
        verbose_name='Material'
        verbose_name_plural='Materiales'
        ordering=['nombre_material',]


#--INSTALACIÓN--
class instalacion(models.Model):
    fecha_instalacion=models.DateField(auto_now=True, verbose_name="Fecha")
    nad_instalacion=models.CharField(max_length=20, verbose_name='NAD de instalación')
    ip_instalacion=models.CharField(max_length=20, verbose_name='IP asignada')
    valor_instalacion=models.IntegerField(verbose_name='Valor Instalación', default=0)
    obs_instalacion=models.TextField(verbose_name='Observación')
    id_cliente=models.ForeignKey(cliente, verbose_name='Nombre cliente', on_delete=models.CASCADE, null=True, blank=True)
    id_inmueble=models.ForeignKey(inmueble, verbose_name='Inmueble de instalación', on_delete=models.CASCADE, null=True, blank=True)
    id_estado=models.ManyToManyField(estado, through='estadoInstalacion', verbose_name='Estado', blank=True)
    id_plan=models.ManyToManyField(plan, through='planInstalacion', verbose_name='Plan', blank=True)
    id_material=models.ManyToManyField(material, through='materialInstalacion', verbose_name='Material', blank=True)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name='Instalación'
        verbose_name_plural='Instalaciones'
        ordering=['fecha_instalacion',]


#--ESTADO_INSTALACIÓN--
class estadoInstalacion(models.Model):
    fecha_estadoInstalacion=models.DateField(verbose_name='Fecha')
    id_estado=models.ForeignKey(estado, verbose_name='Estado', on_delete=models.CASCADE, blank=True, null=True)
    obs_estadoInstalacion=models.TextField(verbose_name='Observacion')
    id_instalacion=models.ForeignKey(instalacion, verbose_name='Instalación', on_delete=models.CASCADE, blank=True,null=True)

    class Meta:
        verbose_name='Estado Instalación'
        verbose_name_plural='Estados de Instalaciones'
        ordering=['id_estado',]



#--MATERIAL_INSTALACIÓN--
class materialInstalacion(models.Model):
    fecha_materialInstalacion=models.DateField(verbose_name='Fecha')
    id_material=models.ForeignKey(material, verbose_name='Material', on_delete=models.CASCADE, null=True,blank=True)
    obs_materialInstalacion=models.TextField(verbose_name='Observación', null=True, blank=True)
    id_instalacion=models.ForeignKey(instalacion, verbose_name='Instalación', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name='Material de Instalación'
        verbose_name_plural='Materiales de Instalación'
        ordering=['id',]


#--PLAN_INSTALACIÓN--
class planInstalacion(models.Model):
    fecha_planInstalacion=models.DateField(verbose_name='Fecha')
    id_plan=models.ForeignKey(plan, verbose_name='Plan', on_delete=models.CASCADE, null=True, blank=True)
    id_instalacion=models.ForeignKey(instalacion, verbose_name='Instalación', on_delete=models.CASCADE, blank=True,null=True)

    class Meta:
        verbose_name='Plan Instalación'
        verbose_name_plural='Planes de Instalaciones'
        ordering=['id_plan',]
    

#--SOLICITUD--
class solicitud(models.Model):
    tipo_solicitud=models.CharField(max_length=20, choices=tipoSolicitud, verbose_name='Tipo de solicitud', default=0, null=True, blank=True)
    fechaInicia_solicitud=models.DateField(auto_now=True, verbose_name='Fecha Inicial')
    obsInicia_solicitud=models.TextField(verbose_name='Observación Inicia')
    fechaFinal_solicitud=models.DateField(verbose_name='Fecha Final', null=True, blank=True)
    obsFinal_solicitud=models.TextField(verbose_name='Observación Final', null=True, blank=True)
    estado_solicitud=models.CharField(max_length=20, verbose_name='Estado de la solicitud', choices=estadoSolicitud, default=0)
    id_instalacion=models.ForeignKey(instalacion, verbose_name='Código Instalación', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.tipo_solicitud
        
    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicitudes'
        ordering=['estado_solicitud',]


#--PAGO DE SERVICIO
class pagoServicio(models.Model):
    fecha_pagoServicio=models.DateField(verbose_name='Fecha')
    valor_pagoServicio=models.IntegerField(verbose_name='Valor Cancelado')
    obs_pagoServicio=models.TextField(verbose_name='Observación', null=True, blank=True)
    id_instalacion=models.ForeignKey(instalacion, verbose_name='Instalación', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name='Pago de Servicio'
        verbose_name_plural='Pagos de Servicio'
        ordering=['fecha_pagoServicio',]
