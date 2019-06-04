import os
from selenium import webdriver
from os import path
if __name__ == "__main__":
    import sys
    sys.path.append(path.join(path.dirname(__file__),'..'))
    from utils import ExcelManage
    from utils import PDFManage
    from utils import HtmlManage
    from utils import FileManage


def GetDriverAtSence(username,password):
        username = username
        password = password
        driver = webdriver.Chrome()
        driver.get("http://www2.sence.cl/otic.htm")
        ###Inicio Sesion###
        driver.find_element_by_id('username1').send_keys(username)
        driver.find_element_by_id('password1').send_keys(password)
        input("Completar Captcha y clickear aceptar: ")
        #driver.find_element_by_id('B2').click()
        return driver

def GetStatuses(driver, idAccion):
        ###Encontrar Consultar ID###
        driver.switch_to.default_content()
        driver.switch_to.frame("superior")
        driver.find_element_by_xpath("//html/body/table/tbody/tr[3]/td[3]/p/a[2]").click()
        ###Consultar la ID SENCE###
        driver.switch_to.default_content()
        driver.switch_to.frame("inferior")
        driver.find_element_by_name("codigoaccion").send_keys(idAccion)
        driver.find_element_by_name("Mostrar").click()
        driver.find_element_by_xpath("//html/body/form/left/div[2]/left/table/tbody/tr[2]/td[2]/small/font/strong[1]/font/u/a").click()
        ###Imprimir###
        driver.switch_to.default_content()
        driver.switch_to.frame("inferior")
        source = driver.page_source
        htmlAddress = HtmlManage.writeHTML(source,idAccion,"html")
        PDFManage.ToPDF(idAccion,htmlAddress,True)
        return

def GetLiquidaciones():
        sheet = FileManage.OpenDialog(fileType = "Excel Spreadsheet",extension = ".xlsx")
        excel = ExcelManage.ExcelConnection(sheet,'Hoja1')
        acciones = excel.collect(1,2)
        excel.close()
        driver = GetDriverAtSence(input("user: "), input("pass: "))
        for i in range(len(acciones)):
                try:
                        idSence = acciones[i]
                        GetStatuses(driver,idSence)
                except:
                        continue
        driver.close
GetLiquidaciones()