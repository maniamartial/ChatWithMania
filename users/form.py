
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

from django.contrib.auth.models import User

# Using the builtin credentials to create a login page


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        # User to login in using username only
        fields = ["username", "password"]


# Using the builtin functionality models to create a register form
class CreateRegisterForm(UserCreationForm):
    class Meta:
        # requirements from teh user
        model = User
        fields = ["username", "email", "password1", "password2"]


# If you want the user to update their credentials
class User_Update_Forms(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]

# You can add any other form..
