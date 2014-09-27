from django.db import models
from catalogos.models import Catalogo

class CatalogoDetalle(models.Model):
	descripcion1  = models.CharField(max_length=255)
	descripcion2 = models.CharField(max_length=255)
	monto1 = models.DecimalField(max_digits=18,decimal_places=2)
	monto2 = models.DecimalField(max_digits=18,decimal_places=2)
	catalogos = models.ForeignKey(Catalogo,default=Catalogo.DEFAULT_PK)