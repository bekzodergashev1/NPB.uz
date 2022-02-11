from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=120, required=True)
    phone = forms.CharField(max_length=20, required=True)
