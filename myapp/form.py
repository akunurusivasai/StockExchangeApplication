import django

from django import forms
from . import models


class Dashboard(forms.ModelForm):
    class Meta:
        model = models.Dash
        fields = ['stocks', 'count']


class KycForm(forms.ModelForm):
    class Meta:
        model = models.KycDetails
        fields = ['Bod']
