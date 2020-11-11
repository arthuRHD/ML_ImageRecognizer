from django import forms
from .models import Image

class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)