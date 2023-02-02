from django import forms
from django.forms import ModelForm
from . models import StdInfo

class StdForm(ModelForm):
    class Meta:
        model = StdInfo
        fields = "__all__"

