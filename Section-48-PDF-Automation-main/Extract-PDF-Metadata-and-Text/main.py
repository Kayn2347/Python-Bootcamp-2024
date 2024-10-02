from PyPDF2 import PdfFileReader


with open("BikeRentalSystem.pdf", "rb") as file:
    pdf_reader = PdfFileReader(file)
    print(pdf_reader.numPages)
    page = pdf_reader.getPage(1)
    text = page.exctractText()
    information = pdf_reader.getDocumentInfo()
    print(f"Author: {information.author}")
    print(f"Title: {information.title}")
    print(f"Creator: {information.creator}")
    print(f"Subject: {information.subject}")
    print(f"Producer: {information.producer}")
    

