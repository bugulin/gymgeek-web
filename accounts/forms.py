from django import forms
from core import material_design

class AboutForm(forms.Form):
    about = forms.CharField(widget=material_design.Textarea, max_length=500, required=False)
