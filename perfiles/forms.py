from django import forms

class PerfilForm(forms.Form):
    foto_perfil = forms.FileField()