from django import forms

class AboutForm(forms.Form):
    about = forms.CharField(max_length=500, required=False)
