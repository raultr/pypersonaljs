from django.db import models

class Catalogo(models.Model):
	DEFAULT_PK=1
	clave  = models.PositiveIntegerField()
	nombre = models.CharField(max_length=255)
	icono = models.ImageField(upload_to='catalogos')

	def __unicode__(self):
	 	return self.nombre