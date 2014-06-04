# -*- encoding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import AbstractBaseUser, _user_has_perm, PermissionsMixin, _user_has_module_perms
from managers import UsuarioManager
from django.db.models.signals import *
from django.dispatch import receiver
from django.core.validators import RegexValidator
from datetime import datetime
from choices import *
try:
	from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
	from django.contrib.contenttypes.generic import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import reversion
from django.db.models.signals import pre_delete, post_save
from django.contrib.admin.models import LogEntry, DELETION, ADDITION, CHANGE
from django.utils.encoding import force_text
import inspect
from django.core.handlers.wsgi import WSGIRequest
from reversion.admin import VersionAdmin
from reversion.models import Version, Revision
import json

class Usuario(AbstractBaseUser, PermissionsMixin):
	usuario = models.CharField(max_length=35, unique=True, db_index=True)
	perfil  = models.CharField(max_length=25, choices=Perfiles)
	email = models.EmailField(max_length=50, unique=True)
	activo = models.BooleanField(default=True, help_text='Activa un usuario para poder entrar en el sistema')
	administrador = models.BooleanField(default=False, help_text='Que usuarios se les permite entrar al administrador')
	objects = UsuarioManager()
	USERNAME_FIELD = 'usuario'
	def get_full_name(self):
		return self.usuario + ' ' + self.perfil
	def get_short_name(self):
		return self.usuario
	def __unicode__(self):
		return self.usuario
	def has_perm(self, perm, obj=None):
		if self.is_superuser:
			return True
		return _user_has_perm(self, perm, obj=obj)
	def has_module_perms(self, app_label):
		return True
	@property
	def is_staff(self):
		return self.administrador
	@property
	def is_active(self):
		return self.activo
	def __unicode__(self) :
	    return '%s' % (self.usuario)
class Categoria(models.Model):
	nombre = models.CharField('Nombre de la categoria',max_length=50)
	def __unicode__(self):
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	precio = models.FloatField()
	categoria = models.ForeignKey('Categoria')
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.id) + self.nombre + str(self.precio)


class Materia_Prima(models.Model):
	clave_mat = models.CharField('Clave',max_length=50)
	descripcion_mat = models.TextField('Descripcion del producto')
	costo1 = models.FloatField('Precio de compra')
	clave_prov = models.ForeignKey('Proveedor')
	clave_up = models.ForeignKey('Unidad_de_presentacion')
	def __unicode__(self):
		return str(self.clave_mat) + self.descripcion_mat + str(self.costo1)


class Proveedor(models.Model):
	clave_prov = models.CharField(max_length=50)
	razonsocial_prov = models.TextField()
	rfc_prov = models.CharField(max_length=25)
	direccion_prov = models.TextField()
	telefono_prov = models.CharField(max_length=30)
	email_prov = models.CharField(max_length=50)
	def __unicode__(self):
		return str(self.clave_prov) + self.razonsocial_prov


class Cliente(models.Model):
	clave_cl = models.CharField('Clave del cliente',max_length=50)
	nombre_cl = models.CharField('Nombre del cliente',max_length=30)
	appaterno_cl = models.CharField('Apellido paterno',max_length=25)
	apmaterno_cl = models.CharField('Apellido materno',max_length=25)
	rfc_prov = models.CharField('RFC',max_length=25)
	direccion_prov = models.TextField('Dirección')
	telefono_prov = models.CharField('Teléfono',max_length=30)
	email_prov = models.CharField('Email',max_length=50)
	def __unicode__(self):
		return str(self.clave_cl) + self.nombre_cl

class Ventas_producto(models.Model):
	
	nombre = models.ForeignKey('Producto')
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.id) + self.nombre.nombre + str(self.cantidad)


class Venta(models.Model):
	producto_venta = models.ManyToManyField('Ventas_producto')
	fecha =  models.DateTimeField(auto_now_add=True)
	clave_cl = models.ForeignKey('Cliente')
	subtotal_venta = models.FloatField()
	iva = models.FloatField()
	total_venta = models.FloatField()
	cantidad = models.IntegerField()
	def __unicode__(self):
		return str(self.fecha) + self.clave_cl.nombre_cl + str(self.total_venta)	

class Receta(models.Model):
	nombre = models.ForeignKey('Producto')
	clave_mat = models.ManyToManyField("Materia_Prima", null = True,blank = True)
	unidad_de_medida = models.CharField(max_length=2,choices=unidadesDmedida,default='kilogramo')
	cantidad = models.FloatField()
	def __unicode__(self):
		return str(self.nombre)


										
class Unidad_de_presentacion(models.Model):
	clave_up = models.CharField(max_length=50)
	descripcion_up = models.TextField()
	cantidad_up = models.CharField(max_length=25)
	presentacion_up=models.CharField(max_length=2,choices=unidadesDmedida,default='kilogramo')
	def __unicode__(self):
		return str(self.clave_up) + self.descripcion_up

class Contacto(models.Model):
	nombre_cl = models.CharField('Nombre del cliente',max_length=30)
	telefono_prov = models.CharField('Teléfono',max_length=30)
	comentario = models.CharField('Comentario', max_length=150)
	email_prov = models.EmailField('Email',max_length=50, unique=True)
	def __unicode__(self):
		return self.nombre_cl


