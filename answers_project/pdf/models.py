from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator

# Create your models here.

class PdfFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self) -> str:
        return str(self.file).split('/')[1]
    

class PdfFileText(models.Model):
    file = models.ForeignKey(PdfFile, on_delete=models.CASCADE)
    file_text = models.TextField()

    # def __str__(self) -> str:
    #     return str(self.file).split('/')[1]
