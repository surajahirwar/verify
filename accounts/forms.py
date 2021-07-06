from django import forms
from django.db.models import fields
from . models import Adduserdata


class Imageform(forms.ModelForm):
    class Meta:
        model = Adduserdata
        fields = ('name', 'course', 'admission_no','image')