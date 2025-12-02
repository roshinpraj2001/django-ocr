OCR Optimizations Used

Preprocessing Images Before OCR

Convert to grayscale

Apply thresholding

Remove noise

Caching OCR Text

OCR is performed once on upload

Stored in DB → avoids re-running OCR every search

Efficient Search

Using icontains on pre-extracted text (fast)

No need to process files during search

Avoiding Large PDF Rerendering

Convert PDFs page-by-page instead of loading whole document

Lightweight Database (SQLite)

