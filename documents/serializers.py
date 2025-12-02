from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'filename', 'file', 'uploaded_date', 'mime_type', 'ocr_text']
        read_only_fields = ['uploaded_date', 'ocr_text']
