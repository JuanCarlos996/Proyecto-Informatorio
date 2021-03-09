from django import forms
from .models import usuario

class registrar_cliente(forms.ModelForm):
	class Meta:
		model = usuario
		widgets = {
        'contraseña': forms.PasswordInput(),
    }
		fields = '__all__'
	
	def __str__(self):
		return super(usuario).__str__()

	