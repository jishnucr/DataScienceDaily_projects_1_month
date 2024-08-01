from django import forms
from django.forms import ModelForm
from .models import webdata

class webform(ModelForm):
    class Meta: # giving more extra features in the user interface
        model = webdata
        fields = '__all__'