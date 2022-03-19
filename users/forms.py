from cProfile import label
from django import forms
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.password_validation import validate_password
from django.core import validators

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
        ]
