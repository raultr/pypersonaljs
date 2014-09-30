import json
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse

from .models import CatalogoDetalle
from catalogos.models import Catalogo

def catalogo_detalle_view(request,catalogod):
	catalogo = get_object_or_404(Catalogo, nombre=catalogod)
	catalogo_detalle= get_list_or_404(CatalogoDetalle, catalogos=catalogo.id)
	print catalogo_detalle

	if catalogo_detalle:
		datos = []
		for det in catalogo_detalle:
			cat = det.catalogos
			dato = {
			    'catalogo': cat.nombre,
				'id': det.id,
				'descripcion1': det.descripcion1,
				'descripcion2': det.descripcion2,
			}
			datos.append(dato)
	#print datos
	datos_json = json.dumps(datos)
	#print datos_json
	for a in datos:
		print a
		print "--"

	return render(request,'catdet.html',{'datos':datos})
#	return HttpResponse(datos_json, content_type='application/json')
#	return HttpResponse("hola mundo")


#	datos_json = json.dumps(datos)

	
	#return render(request,'index.html',{'catdet': catalogo_detalle})
	
	#[<CatalogoDetalle: 1>, <CatalogoDetalle: 2>]

	# datos = {
	# 	'Descripcion': catalogo_detalle.descripcion1,
	# 	'catalogo': catalogo_detalle.catalogo.nombre,
	# }

	# datos_json = json.dumps(datos)

	# return HttpResponse(datos_json, content_type='application/json')