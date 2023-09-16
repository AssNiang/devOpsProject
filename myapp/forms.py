from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    widgets = {
        "username": forms.TextInput(attrs={"class": "form-control"}),
        "email": forms.EmailInput(attrs={"class": "form-control"}),
        "first_name": forms.TextInput(attrs={"class": "form-control"}),
        "last_name": forms.TextInput(attrs={"class": "form-control"}),
    }
