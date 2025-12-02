from django.urls import path
from .views import UploadDocument, ListDocuments, SearchByName, SearchByOCR

urlpatterns = [
    path('upload/', UploadDocument.as_view(), name='upload'),
    path('list/', ListDocuments.as_view(), name='list'),
    path('search/name/', SearchByName.as_view(), name='search_name'),
    path('search/ocr/', SearchByOCR.as_view(), name='search_ocr'),
]
