from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    Nome_Completo = forms.CharField(
        error_messages={'required':'Obrigatório o preenchimento do nome!'},
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Seu nome completo'
            }
        )
    )
    email = forms.EmailField(
        error_messages={'invalid':'Digite um email válido!'},
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite seu email'
            }
        )
    )
    Mensagem = forms.CharField(
        error_messages={'required':'É obrigatório o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua mensagem'
            }
        )
    )


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not 'gmail.com' in email:
            raise forms.ValidationError('O email deve ser do gmail.com')
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Insira seu usuário'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Insira sua senha'
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Insira seu nome de usuário'
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Insira seu email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Insira sua senha'
        }
    ))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Confirme sua senha'
        }
    ))

    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Esse usuário já existe, escolha outro nome.')
        return username
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Esse email já existe, tente outro!')
        return email
    

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('As senhas informadas devem ser iguais!')
        return data