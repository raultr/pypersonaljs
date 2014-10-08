import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Catalogo


class CatalogoView(DetailView):
	model = Catalogo
	context_object_name='catalogo' # especificar como se va a llamar el objeto en las plantillas

	def get_template_names(self): # Regresa el template especificado
		return 'catalogo.html'

def catalogo_view(request,catalogo):
	catalogo= get_object_or_404(Catalogo, nombre=catalogo)

	datos = {
		'id': catalogo.id,
		'clave': catalogo.clave,
		'nombre': catalogo.nombre,
	}
    
	import ipdb; ipdb.set_trace()
	datos_json = json.dumps(datos)

	return HttpResponse(datos_json, content_type='application/json')
#	return render(request,'index.html',{'catalogo': catalogo})
#	return HttpResponse('Ok')

from django.views.generic.detail import DetailView # class base view

