from django import forms

class RegisteredInfo(forms.Form):
    name  = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField()