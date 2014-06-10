# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta, date
from slugify import slugify
import json
from context_processors import *
from forms import *
from models import *
from django.core import serializers

def inicio(request):
	globales = variables_globales(request)
	mensaje= False 
	formulario = LoginForm()
	if not request.user.is_anonymous():
		if globales['HOY'] > EXPIRA:
			mensaje="Periodo de sistema expirado"
			logout(request)
		else:			
			if request.user.perfil == 'Administrador':
				return HttpResponseRedirect(reverse('index'))
	if request.method == "POST":
		formulario = LoginForm(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data["usuario"]
			password = formulario.cleaned_data["password"]
			acceso = authenticate(username=str(usuario), password=str(password))
			if acceso is not None:			
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect(reverse('inicio'))
				else:
					mensaje="Tu usuario esta desactivado"		
			else:
				mensaje="Usuario o contraseña incorrecta"
		else:
			mensaje="Usuario o contraseña incorrecta"
	return render(request, 'login.html',locals())

def salir(request):
        logout(request)
        return HttpResponseRedirect(reverse('inicio'))

def index(request):	
	cliente = Cliente.objects.all()
	contacto= ContactoForm()


	
	return render(request, 'index.html', locals())

def producto(request):
	return render(request, 'productos.html', locals())

def venta(request):
	lista = ((3,2),(2,1))
	lista_productos = []

	if request.method == 'POST':
			if "venta" in request.POST:
				subt = 0
				canttot = 0
				ventas = Venta()
				

				for elementos in lista:				
					producto = Producto.objects.filter(id = elementos[1])[0]
					ventasproducto = Ventas_producto()
					ventasproducto.nombre = producto				
					ventasproducto.cantidad = elementos[0]
					ventasproducto.save()
					producto.cantidad = producto.cantidad - elementos[0]
					producto.save()
					subt = subt + producto.precio * elementos[0]
					canttot = canttot + elementos[0]
					lista_productos.append(ventasproducto)
				
				ventas.clave_cl = Cliente.objects.filter(id = 1)[0]
				ventas.subtotal_venta = subt
				ventas.iva = subt * 0.16
				ventas.total_venta=ventas.subtotal_venta + ventas.iva
				ventas.cantidad = canttot
				ventas.save()
				for elemento_producto in lista_productos:
					ventas.producto_venta.add(elemento_producto)
					ventas.save()

	return render(request, 'ventasx.html', locals())

@csrf_exempt
def validar_login(request):
	usuarios=serializers.serialize('json',Usuario.objects.all())
	usuario = request.POST['usuario']
	password = request.POST['password']
	acceso = authenticate(username=str(usuario), password=str(password))
	if acceso is not None:			
			if acceso.is_active:
				login(request, acceso)
				data = {'access':True, 'mensaje':'Bienvenido'}
			else:
				mensaje="Tu usuario esta desactivado"
				data = {'mensaje':mensaje, 'access':False}	
	else:
		mensaje="Usuario o contraseña incorrecta"
		data = {'access':False, 'mensaje':mensaje, 'usuarios':usuarios}

		print usuarios
	http_response = HttpResponse(json.dumps(data),mimetype='application/json')
	return http_response


@csrf_exempt
def recibir_mensaje(request):
	texto = request.POST['mensaje_de_texto']
	data = {'texto':texto}
	return HttpResponse(json.dumps(data),mimetype='application/json')
	
	



