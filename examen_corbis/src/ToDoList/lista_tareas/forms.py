from django import forms 
from django.forms import ModelForm
from .models import Tareas
from django.contrib.auth.forms import UserCreationForm

from .models import Tareas
    
class FormTarea(forms.ModelForm):
    #vencimiento = forms.DateField(widget=forms.SelectDateWidget())
    
    class Meta:
        model = Tareas
        fields = ['nombre', 'descripcion', 'status']

        
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Ingresar Titulo',
                'class': 'block mx-auto my-5 p-2', }),
            'descripcion': forms.TextInput(attrs={
                'placeholder': 'Escribi tu tarea...',
                'class': 'block mx-auto my-5 w-3/4 h-[50px] p-2', }),
            
            
        }

class CustomUserCreationForm(UserCreationForm):
    pass