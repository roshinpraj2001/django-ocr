from django.db import models

# Create your models here.
class Document(models.Model):
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_date = models.DateTimeField(auto_now_add=True)
    mime_type = models.CharField(max_length=100, blank=True, null=True)
    ocr_text = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.filename