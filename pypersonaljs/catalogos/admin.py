from django.contrib import admin
from django.template.loader import render_to_string
from .models import Catalogo       #. Es la carpeta donde nos encontramos
from catalogos_detalle.models import CatalogoDetalle


class CatalogoInLine(admin.StackedInline): # No permite editar el catalogo_detalles en la misma pantalla de catalogos
	model = CatalogoDetalle
	extra = 1 # Solo un registro adicional para agregar

class CatalogoAdmin(admin.ModelAdmin):
	list_display = ('id','clave','nombre','icono',) # Campos que se mostraran en el administrador
	list_filter = ('nombre',) # Campos por los que podemos filtrar en el administrador
	search_fields = ('nombre',)
	inlines = [CatalogoInLine,] # Solo se admite un nivel de inline
	# def thumb(self, obj):
	# 	return render_to_string('catalogo_icono.html',{'image': obj.icono})

	# thumb.allow_tags = True

admin.site.register(Catalogo,CatalogoAdmin)