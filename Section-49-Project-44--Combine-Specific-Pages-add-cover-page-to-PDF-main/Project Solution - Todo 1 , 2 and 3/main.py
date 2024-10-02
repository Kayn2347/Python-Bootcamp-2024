import os
from PyPDF2 import PdfFileReader, PdfFileWriter

# os.mkdir("Output Files")
# TODO 1 - Get all PDF files in the current directory
pdf_files = []
for file_name in os.listdir("./Input Files"):
    if file_name.endswith(".pdf"):
        pdf_files.append(file_name)

pdf_reader_cover = PdfFileReader("./Input Files/cover_sheet.pdf")
page_cover = pdf_reader_cover.getPage(0)

# TODO 2 - Open all pdf files and read pages
for file_name in pdf_files:
    pdf_reader = PdfFileReader(f"./Input Files/{file_name}")
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(page_cover)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        # TODO 3 - Add cover sheet to the files and save to new directory with new name
        pdf_writer.addPage(page)
    with open(f"./Output Files/{file_name.replace('.pdf', '')}_cover.pdf", "wb") as output:
        pdf_writer.write(output)
