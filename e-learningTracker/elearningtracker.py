import os
from os import path
if __name__ == "__main__":
    import sys
    sys.path.append(path.join(path.dirname(__file__),'..'))
    from utils import HtmlManage as html

def WriteTxt(source, name, folderName, skipLine = False, split = False, extension = ".txt"):
    filename = name + extension
    out = os.path.join(os.getcwd(),folderName)
    os.makedirs(out, exist_ok=True)
    f = open(os.path.join(out,filename),"w+", encoding="utf-8")
    if split:
        lines = source.split("\n")
        line = ""
        for line in lines[1:]:
            splitted = line.split(" ")
        chars = ""
        for chars in splitted:
            #capital = chars.find()              
            line = line + chars + ";"
        f.write(line + "\n")
    if skipLine:
        for i in source:
            f.write(str(i))
        f.write(str(i) + '\n' )
    f.close()
    return

def GetDriver(username, password):
    driver = webdriver.Chrome()
    driver.get("https://aplicaciones.sence.cl/DeclaracionJurada/Identificacion")
    driver.find_element_by_xpath('//*[@id="IDPERFIL"]/option[5]').click()
    driver.find_element_by_id("Rut").send_keys(username)
    driver.find_element_by_id("Clave").send_keys(password)
    driver.find_element_by_id("Enviar").click()
    input("Favor cerrar aviso: ")
    return driver  

def GetAcciones(Qresult):
    import decimal
    acciones = []
    for i in Qresult:
        for j in i:
            if type(j) == type(decimal.Decimal(1)) and j > 1000000:
                acciones.append(int(j))
            if type(j) == str and j == "Liquidada":
                acciones.pop()
    WriteTxt(acciones,"acciones","txt",True)
    return acciones

def QueryElearning(server,user,password,db):
    import pymssql
    query = open(input("Query: "),"r").read()
    conn = pymssql.connect(server=server, user=user, password=password, database=db)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
Qresult = QueryElearning(server=input("server: "),user=input("user: "),password=input("pass: "),db=input("db: "))
acciones = GetAcciones(Qresult)
driver = GetDriver(input("Sence User: "),input("pass: "))
print(acciones)
for i in acciones:
    try:
        driver.find_element_by_id("IDACCION").send_keys(str(i))
        button = driver.find_element_by_xpath('//*[@id="Formulario"]/table[2]/tbody/tr[3]/td/input')
        button.click()
        elements = []
        retries = 50
        while retries != 0:
            try:
                table = driver.find_elements_by_xpath('html/body/div//*[@id="Formulario"]/table[5]')
                print(len(table))
                #source = driver.page_source
                if len(table) != 0:
                    driver.find_element_by_id("IDACCION").clear()
                    elements = table[0].find_elements_by_xpath('.//*')
                    print(elements[0].text)
                    WriteTxt(elements[0].text,str(i),"acciones",split = True, extension = ".csv")     
                    break
                retries = retries - 1
                continue
                #writeHTML(source,str(i),"html")
            except TimeoutException:
                print ("Loading took too much time!")
                retries = retries - 1
                continue
            except NoSuchElementException:
                print ("Unable to find the element")
                retries = retries - 1
                continue
    except:
        input("¿Continuar? Debe de cerrar el mensaje, curso no E-learning.")
        driver.find_element_by_id("IDACCION").clear()