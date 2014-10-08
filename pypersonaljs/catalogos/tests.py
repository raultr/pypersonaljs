from django.test import TestCase
from .models import Catalogo
# Create your tests here.

class TestCatalogo(TestCase):

	def setUp(self):
		self.catalogo = Catalogo.objects.create(id=2,clave=1,nombre="Estatus")

	def test_existe_vista(self):
		res = self.client.get('/catalogos/%d/' % self.catalogo.id) # Error 301 la url esta mal
		self.assertEqual(res.status_code,200) # 200 estado https "Todo ocurrio perfecto"
		self.assertTrue('Estatus' in res.content)

	def test_no_existe_vista(self):
		id_viejo = self.catalogo.id
		print "viejo " + str(id_viejo)
		self.catalogo.delete()
		res = self.client.get('/catalogos/%d/' % id_viejo)
		self.assertEqual(res.status_code,404) # 200 estado https "Todo ocurrio perfecto"
	
	# Tambien se puede crear una prueba que nos diga que solo se puede acceder a una vista logeado