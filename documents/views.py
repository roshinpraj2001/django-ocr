from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document
from .serializers import DocumentSerializer
from .ocr_utils import extract_ocr_text
import mimetypes
from django.conf import settings
import os

class UploadDocument(APIView):
    def post(self, request):
        uploaded_file = request.FILES.get('file')
        if not uploaded_file:
            return Response({"error": "No file provided under key 'file'."}, status=400)

        mime_type = mimetypes.guess_type(uploaded_file.name)[0] or ''
        doc = Document.objects.create(
            filename=uploaded_file.name,
            file=uploaded_file,
            mime_type=mime_type
        )

        file_path = doc.file.path  # full path on disk
        # If you need poppler_path on Windows, pass it here: poppler_path="C:\\path\\to\\poppler\\bin"
        try:
            ocr_text = extract_ocr_text(file_path)
            doc.ocr_text = ocr_text
            doc.save()
        except Exception as e:
            # don't fail upload just because OCR had an issue
            return Response({"error": f"Uploaded but OCR failed: {str(e)}"}, status=500)

        return Response(DocumentSerializer(doc).data, status=201)


class ListDocuments(APIView):
    def get(self, request):
        docs = Document.objects.all().order_by('-uploaded_date')
        return Response(DocumentSerializer(docs, many=True).data)


class SearchByName(APIView):
    def get(self, request):
        q = request.GET.get('q', '')
        docs = Document.objects.filter(filename__icontains=q)
        return Response(DocumentSerializer(docs, many=True).data)


class SearchByOCR(APIView):
    def get(self, request):
        q = request.GET.get('q', '')
        docs = Document.objects.filter(ocr_text__icontains=q)
        return Response(DocumentSerializer(docs, many=True).data)
