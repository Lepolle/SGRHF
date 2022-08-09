from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Rol (models.Model):
    nombre = models.CharField()


class CategoriaOcupacional(models.Model):
    nombre = models.CharField()


class GrupoEscala(models.Model):
    nombre = models.CharField()


class Clasificacion (models.Model):
    nombre = models.CharField()


class NivelPreparacion (models.Model):
    nombre = models.CharField()


class FuenteProcedencia (models.Model):
    nombre = models.CharField()


class MotivoBaja (models.Model):
    nombre = models.CharField()


class Res272006 (models.Model):
    nombre = models.CharField()


class Res492019 (models.Model):
    nombre = models.CharField()


class Provincia (models.Model):
    nombre = models.CharField()


class Municipio (models.Model):
    nombre = models.CharField()
    provincia = models.ForeignKey(Provincia, related_name='provincia',
                                  on_delete=models.DO_NOTHING)


class Unidad (models.Model):
    nombre = models.CharField()
    municipio = models.ForeignKey(Municipio, related_name='municipio',
                                  on_delete=models.DO_NOTHING)


class UnidadOrganizativa (models.Model):
    nombre = models.CharField()
    unidad = models.ForeignKey(Unidad, related_name='unidad',
                               on_delete=models.DO_NOTHING)


class Cargo (models.Model):
    nombre = models.CharField()
    categoriaOcupacional = models.ForeignKey(CategoriaOcupacional, related_name='categoria ocupacional',
                                             on_delete=models.DO_NOTHING)
    grupoEscala = models.ForeignKey(GrupoEscala, related_name='grupo escala',
                                    on_delete=models.DO_NOTHING)
    clasificacion = models.ForeignKey(Clasificacion, related_name='clasificacion',
                                      on_delete=models.DO_NOTHING)


class CargoNivelPreparacion (models.Model):
    cargo = models.ForeignKey(Cargo, related_name='cargo',
                              on_delete=models.DO_NOTHING)
    nivelPreparacion = models.ForeignKey(NivelPreparacion, related_name='nivel de preparacion',
                                         on_delete=models.DO_NOTHING)


class Plaza (models.Model):
    nombre = models.CharField()
    cantidad = models.IntegerField()
    necesarios = models.IntegerField()
    cubiertas = models.IntegerField()
    mision = models.IntegerField()
    unidadOrganizativa = models.ForeignKey(UnidadOrganizativa, related_name='unidad organizativa',
                                           on_delete=models.DO_NOTHING)
    cargo = models.ForeignKey(Cargo, related_name='cargo',
                              on_delete=models.DO_NOTHING)
    nivelPreparacion = models.ForeignKey(NivelPreparacion, related_name='nivel de preparacion',
                                         on_delete=models.DO_NOTHING)
    res272006 = models.ForeignKey(Res272006, related_name='resolucion 272006',
                                  on_delete=models.DO_NOTHING)
    res492019 = models.ForeignKey(Res492019, related_name='resolucion 492019',
                                  on_delete=models.DO_NOTHING)


class Personal (models.Model):
    nombre = models.CharField()
    apellidos = models.CharField()
    sexo = models.CharField()
    ci = models.CharField(max_length=11)
    direccionParticular = models.CharField()
    fechaAlta = models.DateField()
    fechaBaja = models.DateField()
    fuenteProcedencia = models.ForeignKey(FuenteProcedencia, related_name='fuente de procedencia',
                                          on_delete=models.DO_NOTHING)
    motivoBaja = models.ForeignKey(MotivoBaja, related_name='motivo de baja',
                                   on_delete=models.DO_NOTHING)
    plaza = models.ForeignKey(Plaza, related_name='plaza',
                              on_delete=models.DO_NOTHING)


class Usuario (AbstractUser):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ci = models.CharField(max_length=11)
    rol = models.ForeignKey(Rol, related_name='rol', on_delete=models.DO_NOTHING)


USERNAME_FIELD = 'nombre'
REQUIRED_FIELDS = ['username', 'password']
!!!!!!!!!!!!TERMINA LA AUTH!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!