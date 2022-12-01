from django import forms

class TematicaFormulario(forms.Form):
    nombre_tema=forms.CharField()
    autor=forms.CharField()
    codigo=forms.CharField()

class ContactoFormulario(forms.Form):
    nombre=forms.CharField()
    correo=forms.CharField()
    descripcion=forms.CharField()


class UsuarioFormulario(forms.Form):
    nombre=forms.CharField()
    correo=forms.CharField()
    nacionalidad=forms.CharField()
        