from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class formName(forms.Form):
    name = forms.CharField(required="True")
    email = forms.EmailField(required="True")
    text = forms.CharField(widget=forms.Textarea, required="True")

    botcatcher = forms.CharField(required="False",
                    widget=forms.HiddenInput, validators=
                    [validators.MaxLengthValidator(0)])


 
     

     