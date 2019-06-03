import PyPDF2

class PDF2Txt():

    def __init__(self,pdf):
        self.pdf = pdf
        self.pdfObj = open(self.pdf,'rb')
        self.CompleteStr = ""
        self.AllPages()
        
    def Read(self):
        return self.CompleteStr

    def AllPages(self):
        self.pdfRead = PyPDF2.PdfFileReader(self.pdfObj)
        numPages = self.pdfRead.numPages
        for i in range(numPages):
            page = self.pdfRead.getPage(i)
            self.CompleteStr = self.CompleteStr + page.extractText()


if __name__== "__main__":
    PDF2Txt(None)
