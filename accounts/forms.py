from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input username'
    }))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Input password'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('This username not found')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Invalid password')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user is inactive')
        return super().clean(*args, **kwargs)
