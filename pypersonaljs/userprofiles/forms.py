from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationEmailForm(UserCreationForm):
	email = forms.EmailField()

	class Meta: # Los metadatos del modelo son cualquier cosa que no sea un campo, como opciones de ordenamiento etc.
		model = User
		fields = ('username','email')
