import sence
import os
from datetime import datetime, date, time
from utils import HtmlManage as html

now = datetime.now()
now = str(now.strftime("%d-%b-%Y-%I.%M%p"))
codigoSence = str(input("Ingresar Codigo Sence (10 Digitos): "))
sen = sence.SENCE()
Source = sen.codCurso(codigoSence)
registry = codigoSence +"-" + now
htmlPath = html.writeHTML(Source,registry,"html")
os.startfile(htmlPath)