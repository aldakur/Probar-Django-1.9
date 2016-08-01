from django import forms
from .models import Registrado


class RegistradoForm(forms.ModelForm):
    class Meta:
    	model = Registrado
    	fields = ["email", "nombre", "media"] # Con corchetes es una lista y con {} llaves es un diccionario

    def clean_email(self):
    	email = self.cleaned_data.get("email")
    	# print email # Imprime el dato email del formulario de forma limpia
    	email_base, proveedor = email.split("@") # split divide omando como referencia la @ con lo cual email_base recibe los valores a la izquierda de @ y proveedor a la derecha
    	dominio, extension = proveedor.split(".")
    	if not extension == "edu":
    		raise forms.ValidationError("Utilice emails con extension .edu")
    	return email


#class RegForm(forms.Form):
	#nombre_form = forms.CharField(max_length=100)
	#edad = forms.IntegerField()