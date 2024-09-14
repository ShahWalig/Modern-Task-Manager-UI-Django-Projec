from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

# Form for user registration
class CreateUserForms(UserCreationForm):
    class Meta:
        model = User  # Specifies the model associated with this form
        fields = ['username', 'email', 'password1', 'password2']  # Fields to include in the form

# Form for user login
class LoginForm(AuthenticationForm):
    # Customizing the username field to use a text input widget
    username = forms.CharField(widget=TextInput())
    # Customizing the password field to use a password input widget (hides text)
    password = forms.CharField(widget=PasswordInput())
