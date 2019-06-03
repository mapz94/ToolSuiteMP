import os 
import pdfkit
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
           
def ToPDF(filename,filepath,toPrint):
    name = filename[0:-4] + "pdf"
    out = os.path.join(os.path.dirname(__file__),"pdf")
    os.makedirs(out, exist_ok=True)
    print(out)
    try:
        pdfkit.from_file(filepath, os.path.join(out,name))
    except:
        pass
    if toPrint == True:
        Printer(filepath)

def naturalSort(objList):
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(objList, key = alphanum_key)

def mergerNatural():
    files = os.listdir()
    files_pdf = [i for i in files if i.endswith('.pdf')]
    files_pdf = naturalSort(files_pdf)
    print(files_pdf)
    merger("Merged.pdf",files_pdf)

def makePDF():
    pdfkit

def Printer(file):
    os.startfile(file, "print")


#merges PDF Files in folder
if __name__ == "__main__":
    path = os.path.dirname(__file__)
    files = os.listdir(path)
    files_html = [i for i in files if i.endswith('.html')]
    for html in files_html:
        filepath = os.path.realpath(html)
        print(filepath)
        ToPDF(html,filepath,False)
    wd = os.path.join(os.getcwd(),"pdf")
    files = os.listdir(path)
    files_pdf = [i for i in files if i.endswith('.pdf')]
    merger(os.path.join(path,"Merged.pdf"),[])