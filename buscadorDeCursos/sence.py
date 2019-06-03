import os
from selenium import webdriver
from utils import PDFManage as PdfManage


class SENCE():

    def status(self,username,password, idAccion):
        username = input("user: ")
        password = input("pass: ")
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver.get("http://www2.sence.cl/otic.htm")
        ###Inicio Sesion###
        driver.find_element_by_id('username1').send_keys(username)
        driver.find_element_by_id('password1').send_keys(password)
        driver.find_element_by_id('B2').click()
        ###Encontrar Consultar ID###
        driver.switch_to.default_content()
        driver.switch_to.frame("superior")
        driver.find_element_by_xpath("//html/body/table/tbody/tr[3]/td[3]/p/a[2]").click()
        ###Consultar la ID SENCE###
        driver.switch_to.default_content()
        driver.switch_to.frame("inferior")
        driver.find_element_by_name("codigoaccion").send_keys(idAccion)
        #IDSence.send_keys(input('ID de Accion: '))
        driver.find_element_by_name("Mostrar").click()
        driver.find_element_by_xpath("//html/body/form/left/div[2]/left/table/tbody/tr[2]/td[2]/small/font/strong[1]/font/u/a").click()
        ###Imprimir###
        driver.switch_to.default_content()
        driver.switch_to.frame("inferior")
        source = driver.page_source
        driver.close()
        return source

    def codCurso(self, CodigoCurso):
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        url = "http://otec.sence.cl/datoscurso.html?rut=%20&nom=%20&es=23&ar=01&cod=" + (str(CodigoCurso))
        print (url)
        driver.get(url)
        source = driver.page_source
        driver.close()
        return source

if __name__ == "__main__":
    try:
        SENCE().status(NULL,NULL,NULL)
    except:
        print("Not Available")
