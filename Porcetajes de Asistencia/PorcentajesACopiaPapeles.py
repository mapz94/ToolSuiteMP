import PDF2Text
import pyperclip
from utils import FileManage

pdf = FileManage.OpenDialog("Pdf",".pdf")
text = PDF2Text.PDF2Txt(pdf.Get())
certificado = text.Read()

index = [i for i, letter in enumerate(certificado) if letter == '%']
percentages = ""
for i in range(len(index)):
    #print("index")
    num = int(certificado[index[i]-4:index[i]])
    percentages = percentages + str(num) + '\n'

pyperclip.copy(percentages)
print(percentages)
print("Pegar en SICAP: ")

input()
