import os 
from PyPDF2 import PdfFileReader, PdfFileWriter
import re


def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
                pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)

def naturalSort(objList):
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(objList, key = alphanum_key)

wd = os.getcwd()
files = os.listdir()
files_pdf = [i for i in files if i.endswith('.pdf')]
files_pdf = naturalSort(files_pdf)
print(files_pdf)
merger("Merged.pdf",files_pdf)