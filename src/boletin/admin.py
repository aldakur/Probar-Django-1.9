from django.contrib import admin
from .models import Registrado
from .forms import RegistradoForm

# Register your models here.


class AdminRegistrado(admin.ModelAdmin):
	list_display = ["__unicode__", "nombre", "codigo_postal", "timestamp"] # __unicode__ nos devuelve el email pq asi lo tenemos definido en el models.py
	form = RegistradoForm
	#class Meta:
		#model = Registrado


admin.site.register(Registrado, AdminRegistrado)