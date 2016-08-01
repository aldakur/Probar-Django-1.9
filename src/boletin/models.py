from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
	nombre = models.CharField(max_length=120, blank=True, null=True) #blank para validar formulario. Null es para la Base de Datos. Por defecto son False
	email = models.EmailField()
	codigo_postal = models.IntegerField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False) # al crear se crea la fecha y nunca mas se actualiza
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True) # Cada vez que alguien actualiza algo queremos que se actualice esta variable
	media = models.FileField(upload_to='myfolder/', blank=True, null=True) # no colocar la barra antes de la carpeta. Siempre depues


	def __unicode__(self): # Python 3 __str__
		return self.email