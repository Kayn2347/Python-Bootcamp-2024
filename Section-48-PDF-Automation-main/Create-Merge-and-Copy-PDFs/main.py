from PyPDF2 import PdfFileReader, PdfFileWriter


# with open("BikeRentalSystem.pdf", "rb") as file, open("output.pdf", "wb") as output:
#     pdf_reader = PdfFileReader(file)
#     page = pdf_reader.getPage(2)
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(page)
#     pdf_writer.write(output)
    

# with open("BIGO.pdf", "rb") as file, open("output.pdf", "wb") as output, \
#        open("combined.pdf", "wb") as combined:
#     pdf_reader = PdfFileReader(file)
#     page = pdf_reader.getPage(0)
#     pdf_reader1 = PdfFileReader(output)
#     page1 = pdf_reader.getPage(0)
#     pdf_writer = PdfFileWriter()
#     pdf_writer.addPage(page)
#     pdf_writer.addPage(page1)
#     pdf_writer.writer(combined)


with open("BIGO.pdf", "rb") as bigo, open("RangeFunction.pdf", "wb") as range_func, \
       open("together.pdf", "wb") as together:
     pdf_writer = PdfFileWriter()
     pdf_reader_o = PdfFileReader(bigo)
     pdf_reader_r = PdfFileReader(range_func)
     for page_num in range(pdf_reader_o.numPages):
         page_o = pdf_reader_o.getPage(page_num)
         pdf_writer.addPage(page_o)
     for page_num in range(pdf_reader_r.numPages):
         page_r = pdf_reader_r.getPage(page_num)
         pdf_writer.addPage(page_r)
     pdf_writer.write(together)