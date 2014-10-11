from rest_framework import serializers
from .models import CatalogoDetalle

class CatalogoDetalleSerializer(serializers.HyperlinkedModelSerializer):
		es_pais1 = serializers.SerializerMethodField('es_pais2')
	
		def es_pais2(self,obj):
			return obj.es_pais()

		class Meta:
			model = CatalogoDetalle
			fields = ('id','descripcion1','descripcion2','es_pais1')