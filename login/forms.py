from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=256, required=True, help_text='Please, inform us your First Name')
    last_name = forms.CharField(max_length=256, required=True, help_text='Please, inform us your Last Name')
    email = forms.EmailField(max_length=256, help_text='Inform a Valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
