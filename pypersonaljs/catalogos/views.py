import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Catalogo

def catalogo_view(request,catalogo):
	catalogo= get_object_or_404(Catalogo, nombre=catalogo)

	datos = {
		'id': catalogo.id,
		'clave': catalogo.clave,
		'nombre': catalogo.nombre,
	}

	datos_json = json.dumps(datos)

	return HttpResponse(datos_json, content_type='application/json')
#	return render(request,'index.html',{'catalogo': catalogo})
#	return HttpResponse('Ok')
