from django.shortcuts import render
from .forms import RegistradoForm
from .models import Registrado

# Create your views here.
# La vista o view obtiene datos de acurdo a lo pasado en la URL y como norma general cargara un template
# y devolvera ese template ejecutando nuestro codigo (request) (response)

def inicio(request):
	titulo = "Bienvenidos"
	form = RegistradoForm(request.POST or None, request.FILES or None) # or None para que no aparezca lo de las validaciones. O pasa por las validaciones o no. request.FILES para los archivos
	queryset = Registrado.objects.all()

	for obj in queryset:
		print obj.nombre
		print obj.email
		print obj.id # Este id es generado automaticamente por Models.forms

	context = {
		"titulo": titulo,
		"form": form,
		"queryset": queryset
	}

	if form.is_valid():
		instance = form.save(commit=False) # commit=False es para no guardar en la base de datos
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		form.save()

		context = {
			"titulo": "Gracias %s, ya se ha registrado." %(nombre)
		}
		if not nombre:
			context = {
				"titulo": "Gracias %s, ya se ha registrado." %(email)
			}
	return render(request, "inicio.html", context) # {} es el diccionario vacio. El contexto.
	# if request.user.is_authenticated():
	# 	titulo = "Hola, %s!" %(request.user)


	#if form.is_valid():
		#print form.cleaned_data # Devuelve por consola {'edad': 2, 'nombre': u'karlita'}
		#print form_dicc.get("nombre") # devuelve por consola el nombre insertado en el campo nombre del formulario
		#form_data = form.cleaned_data # Datos del formulario limpios
		#abc = form_data.get("nombre_form")
			#obj2 = Registrado()
			#obj2.nombre = abc
			#obj2.save()
		# Las tres lineas anteriores se pueden resumir en una:
		#obj = Registrado.objects.create(nombre=abc) # Crea y guarda el objeto en la Base de datos

def sobre(request):
	titulo = "Sobre nosotros"

	context = {
		"titulo": titulo,
	}
	
	return render(request, "sobre.html", context) # {} es el diccionario vacio. El contexto.


	