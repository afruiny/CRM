from django import forms 
from .models import Leads
from leads.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UsernameField

class LeadCreateForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)

class LeadModelCreateForm(forms.ModelForm):

    class Meta:

        model = Leads
        fields = (
            '__all__'
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}






