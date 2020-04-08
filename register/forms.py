from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(str(self.cleaned_data['email'])+" is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ["name","username","email","password1","password2"]