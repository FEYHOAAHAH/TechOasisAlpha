from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from userapp.models import UserMy

class RegistrationForm(UserCreationForm):

    class Meta:
        model = UserMy
        fields = ('first_name', 'last_name', 'username', 'email', 'address', 'user_phone_number')


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserMy

