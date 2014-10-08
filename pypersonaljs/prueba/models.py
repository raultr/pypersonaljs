from django.db import models

# Create your models here.
class CatalogoPrueba(models.Model):
	id = models.AutoField('ID', primary_key=True)
	clave  = models.PositiveIntegerField()
	nombre = models.CharField(max_length=255)
	icono = models.FileField(upload_to='catalogos')