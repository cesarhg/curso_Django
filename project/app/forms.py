#encoding:utf-8
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from datetime import datetime
from models import *    

User = get_user_model()
class CrearusuarioForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password", widget=forms.PasswordInput, help_text="Introduce de nuevo tu password")

    class Meta:
        model = Usuario
        fields = ('usuario', 'email', 'perfil', 'user_permissions', 'is_superuser')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las passwords no coinciden")
        return password2
    def save(self, commit=True):
        user = super(CrearusuarioForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CambiarusuarioForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="<a href='password/'>Cambiar contraseña</a>")
    class Meta:
        model = Usuario
    def clean_password(self):
        return self.initial['password']

class LoginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Usuario o email', 'type':'text', 'autofocus':'True'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password','type':'password',}), required=True)


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
    

