from PyPDF2 import PdfFileReader, PdfFileWriter


# file_pdf = PdfFileReader("together.pdf")
# for page in range(file_pdf.getNumPages()):
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(file_pdf.getPage(page))
#     output = f"SplitFile{page}.pdf"
#     with open(output, "wb") as output_pdf:
#         pdf_writer.write(output_pdf)


# pdf_reader = PdfFileReader("together.pdf")
# pdf_writer = PdfFileWriter()
# page1 = pdf_reader.getPage(0).rotateClockwise(90)
# pdf_writer.addPage(page1)
# page2 = pdf_reader.getPage(1).rotateClockwise(90)
# pdf_writer.addPage(page2)
# with open("rotated_file.pdf", "wb") as rf:
#   pdf_writer.write(rf)


watermark = PdfFileReader("sample.pdf")
watermark_page = watermark.getPage(0)
pdf_reader = PdfFileReader("together.pdf")
pdf_writer = PdfFileWriter()

for page in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page)
    page.mergePage(watermark_page)
    pdf_writer.addPage(page)

with open("watermark.pdf", "wb") as output:
    pdf_writer.write(output)