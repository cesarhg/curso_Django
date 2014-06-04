# -*- encoding: utf-8 -*-
from forms import *
from models import *
from project.settings.base import EMPRESA, EXPIRA, NOMBRE

def variables_globales(request):
	try:
		USUARIO = request.user
	except:
		USUARIO = 'ANONIMO'
	return {'EMPRESA' : EMPRESA, 'HOY': datetime.date(datetime.now()), 'USUARIO':USUARIO, 'NOMBRE':NOMBRE}