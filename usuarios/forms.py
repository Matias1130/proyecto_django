from django import forms
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,PasswordChangeForm
from django.contrib.auth.models import User 


class FormularioUsuario(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    biografia =forms.CharField(label='Contanos brevemente un poco de tu vida')
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','biografia']
        help_texts = {key: '' for key in fields}


class FormularioParaEdicionDePerfil(UserChangeForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    biografia = forms.CharField(label='Cambia los datos de tu biografia')
    password = None
    avatar = forms.ImageField(required=False,)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','avatar','biografia']
        
    
class FormularioCambioContraseña(PasswordChangeForm):
    old_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña actual'})
    )
    new_password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su nueva contraseña'})
    )
    new_password2 = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirme su nueva contraseña'})
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']