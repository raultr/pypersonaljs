from django.db import models
from decimal import *
from catalogos.models import Catalogo

class CatalogoDetalle(models.Model):
	descripcion1  = models.CharField(max_length=255)
	descripcion2 = models.CharField(max_length=255, blank=True)
	monto1 = models.DecimalField(max_digits=18,decimal_places=2,default=Decimal('0.00'))
	monto2 = models.DecimalField(max_digits=18,decimal_places=2,default=Decimal('0.00'))
	catalogos = models.ForeignKey(Catalogo,default=Catalogo.DEFAULT_PK)

	def codigo(self): # Campo calculado en el administrador
		return str(self.catalogos.id) + '-' + str(self.id) 

	def es_pais(self):
		return self.catalogos.nombre == "Pais"

#       Investigar para que sirve @staticmethod
#	@staticmethod
#	def autocomplete_Search_fields():
#		return ("descripcion1__icointains","descripcion2__icontains")
		
	def __unicode__(self):
		return str(self.id)