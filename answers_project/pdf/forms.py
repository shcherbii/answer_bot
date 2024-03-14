from django import forms
from .models import PdfFile

class PdfFileForm(forms.ModelForm):

    class Meta:
        model = PdfFile
        fields = ('file', )