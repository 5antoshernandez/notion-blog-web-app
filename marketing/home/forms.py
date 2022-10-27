from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Contact
from django.core import validators


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'company_name', 'details']

