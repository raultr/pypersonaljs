from django.contrib import admin
from django.template.loader import render_to_string
from .models import Catalogo       #. Es la carpeta donde nos encontramos


class CatalogoAdmin(admin.ModelAdmin):
	list_display = ('id','clave','nombre','icono',) # Campos que se mostraran en el administrador
	list_filter = ('nombre',) # Campos por los que podemos filtrar en el administrador
	search_fields = ('nombre',)
	# def thumb(self, obj):
	# 	return render_to_string('catalogo_icono.html',{'image': obj.icono})

	# thumb.allow_tags = True

admin.site.register(Catalogo,CatalogoAdmin)