import fitz

def extract_pdf_text(file):
    document = fitz.open(stream=file.read(), filetype="pdf")
    text = ""

    for page in document:
        text+=page.get_text()

    document.close()

    return text    