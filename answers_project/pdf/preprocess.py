import ironpdf
from .models import PdfFileText

ironpdf.License.LicenseKey = 'change me' 

def read_pdf(file):
    path = str(file.file.path)
    pdf = ironpdf.PdfDocument.FromFile(path)
    page_count = pdf.PageCount
    for page in range(page_count):
        extracted_text_page = pdf.ExtractTextFromPage(page)
        PdfFileText.objects.create(file = file, file_text = extracted_text_page)
