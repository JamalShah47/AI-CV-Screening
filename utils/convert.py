import PyPDF2
import docx
from tempfile import NamedTemporaryFile

def extract_text_from_pdf(file):
    text = ''
    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        file.save(temp_file.name)
        with open(temp_file.name, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
    return text

def extract_text_from_docx(file):
    
    with NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
        file.save(temp_file.name)
        doc = docx.Document(temp_file.name)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
    return text
