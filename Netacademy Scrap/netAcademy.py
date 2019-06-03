import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils import HtmlManage as html

def scrapNetAcademy(language):
    username = input("NetAcademy User: ")
    password = input("NetAcademy Pass: ")
    driver = webdriver.Chrome()
    driver.get("https://www.netacad.com/login/")
    ###Inicio Sesion###
    driver.find_element_by_id('_58_INSTANCE_fm_login').send_keys(username)
    driver.find_element_by_id('_58_INSTANCE_fm_password').send_keys(password)
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//*[@id="buttons-container"]/button').click()
    driver.get("https://static-course-assets.s3.amazonaws.com/ITE6/"+ language+"/index.html#0.0.1.1")
    driver.switch_to.default_content()
    timeout = 60
    WebDriverWait(driver, timeout)
    input("Passed? ")
    lastSource = ""
    while True:
        name = driver.find_element_by_id("breadcrumbs-page-li").text
        print(name) 
        driver.switch_to.frame(driver.find_element_by_id("frame"))
        source = driver.page_source
        if lastSource == source:
            break
        #print(source)
        html.writeHTML(source,name,language)
        lastSource = source
        driver.switch_to.default_content()
        driver.find_element_by_id("page-menu-next-button").click()
    #driver.close()
    return
if __name__ == "__main__":
    scrapNetAcademy(input("Language es en fr: "))
