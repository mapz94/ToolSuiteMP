import PDF2Text
import pyperclip
from os import path

if __name__ == "__main__":
    import sys
    sys.path.append(path.join(path.dirname(__file__),'..'))
    from utils import FileManage

    pdf = FileManage.OpenDialog("Pdf",".pdf")
    text = PDF2Text.PDF2Txt(pdf)
    certificado = text.Read()

    index = [i for i, letter in enumerate(certificado) if letter == '%']
    percentages = ""
    for i in range(len(index)):
        #print("index")
        num = int(certificado[index[i]-4:index[i]])
        percentages = percentages + str(num) + '\n'

    print(percentages)
    print("Pegar en SICAP: ")
    pyperclip.copy(percentages)
    input()
   