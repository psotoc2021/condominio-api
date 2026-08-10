from django import forms
from django.contrib.auth.models import User
from .models import Documento


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,
        label="Contraseña"
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ["titulo", "descripcion", "tipo", "archivo"]