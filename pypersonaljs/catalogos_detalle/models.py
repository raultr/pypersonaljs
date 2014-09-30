from django.db import models
from decimal import *
from catalogos.models import Catalogo

class CatalogoDetalle(models.Model):
	descripcion1  = models.CharField(max_length=255)
	descripcion2 = models.CharField(max_length=255, blank=True)
	monto1 = models.DecimalField(max_digits=18,decimal_places=2,default=Decimal('0.00'))
	monto2 = models.DecimalField(max_digits=18,decimal_places=2,default=Decimal('0.00'))
	catalogos = models.ForeignKey(Catalogo,default=Catalogo.DEFAULT_PK)

	def __unicode__(self):
		return str(self.id)