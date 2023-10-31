from django import forms

class mi_formulario(forms.Form):
    nombre = forms.CharField(max_length=255)
    correo = forms.EmailField()
    mensaje = forms.CharField(max_length=255)