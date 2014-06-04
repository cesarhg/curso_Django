import os, sys, site
from os.path import abspath, dirname
from sys import path
try:
	from project.settings.base import VIRTUALENV, NOMBREDEUSUARIO
except:
	pass
	
try:
	SITE_ROOT = dirname(dirname(abspath(__file__)))
	path.append(SITE_ROOT)
	# Tell wsgi to add the Python site-packages to its path. 
	site.addsitedir('/home/'+ NOMBREDEUSUARIO +'/.virtualenvs/'+ VIRTUALENV +'/lib/python2.7/site-packages')
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.produccion")
	activate_this = os.path.expanduser("~/.virtualenvs/"+ VIRTUALENV +"/bin/activate_this.py")
	execfile(activate_this, dict(__file__=activate_this))
	# Calculate the path based on the location of the WSGI script
	project = '/home/'+ NOMBREDEUSUARIO +'/webapps/'+ VIRTUALENV +'/project/project/'
	workspace = os.path.dirname(project)
	sys.path.append(workspace)
except: 
	pass

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

