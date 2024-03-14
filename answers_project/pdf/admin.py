from django.contrib import admin
from .models import PdfFile, PdfFileText
# Register your models here.

admin.site.register(PdfFile)
admin.site.register(PdfFileText)
