from PyPDF2 import PdfFileReader, PdfFileWriter


pdf_reader = PdfFileReader("encrypted.pdf")
# pdf_reader.decrypt("test123")
page1 = pdf_reader.getPage(0)
print(page1.extractText())










