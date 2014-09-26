from django.db import models

class Catalogo(models.Model):
	clave  = models.PositiveIntegerField()
	nombre = models.CharField(max_length=255)
