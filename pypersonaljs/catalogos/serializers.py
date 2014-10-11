from rest_framework import serializers
from .models import Catalogo

class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
			model = Catalogo