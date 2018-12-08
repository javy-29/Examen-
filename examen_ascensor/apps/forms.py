from django import forms
from .models import Tecnico, Orden

class LoginForm (forms.ModelForm):
    contraseña = forms.CharField (widget=forms.PasswordInput)
    class Meta:
        model = Tecnico
        fields =[
            'usuario',
            'contraseña',
        ]               
            
            
class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = [
            'Cliente',
            'fecha',
            'hora_inicio',
            'hora_termino',
            'id_ascensor',
            'modelo_ascensor',
            'fallas_detectadas',
            'reparaciones',
            'piezas',
            'Tecnico'
        ]

        widgets = {
            'fecha': forms.TextInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TextInput(attrs={'type': 'time'}),
            'hora_termino': forms.TextInput(attrs={'type': 'time'}),
            }
