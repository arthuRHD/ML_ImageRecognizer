from django import forms
from .models import Image

class UploadDocumentForm(forms.Form):
    file = forms.ImageField(allow_empty_file=False)
