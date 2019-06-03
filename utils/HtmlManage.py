import os
import html2text #Pip Package
import PyPDF2

def to_text(html, rehtml=False):
    parser = html2text.HTML2Text()
    parser.wrap_links = False
    parser.skip_internal_links = True
    parser.inline_links = True
    parser.ignore_anchors = True
    parser.ignore_images = True
    parser.ignore_emphasis = True
    parser.ignore_links = True
    text = parser.handle(html)
    text = text.strip(' \t\n\r')
    if rehtml:
        text = text.replace('\n', '<br/>')
        text = text.replace('\\', '')
    return text 

def writeHTML(source, name, folderName):
    filename = name + ".html"
    out = os.path.join(os.path.dirname(__file__),folderName)
    os.makedirs(out, exist_ok=True)
    address = os.path.join(out,filename)
    f = open(address,"w+", encoding="utf-8")
    f.write(source)
    f.close()
    return address

#Converts .html files to .txt
def convert():
    cwd = os.getcwd()
    fileList = os.listdir()

    htmlList = [i for i in fileList if i.endswith('.html')]
    for i in htmlList:
        print(i)
        read = open(i,"r",encoding = "utf-8").read()
        os.makedirs("text", exist_ok=True)
        f = open(os.path.join(cwd,"text",i[0:len(i)-5]+".txt"), "w+", encoding = "utf-8")
        f.write(to_text(read))
        f.close()

if __name__ == "__main__":
    convert()