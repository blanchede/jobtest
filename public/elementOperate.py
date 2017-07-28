#!/user/bin/env python
# -*-coding:utf-8-*-
#定义一些元素的操作

from selenium.webdriver.common.by import By
from time import sleep
import public.publicMethod
from selenium.webdriver.common.keys import Keys

driver = public.publicMethod.driver
class ElementMethod():
    def inputText(self,xpath,text):
        sleep(1)
        driver.find_element(By.XPATH, xpath).send_keys(text)

    def clickElement(self,xpath):
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, xpath).click()

    #先判断folder是否打开，未打开就点击打开
    def open_Folder(self,folderXpath,clickXpath):
        folder = driver.find_element(By.XPATH, folderXpath)
        if folder.get_attribute("class") == "fa fa-folder-open":
            #folder已打开
            print("文件夹已打开，不用再点击")
        else:
            driver.find_element(By.XPATH,clickXpath).click()

    #判断弹窗是否还在界面上显示
    def isPopupExist(self,xpath):
        sleep(1)
        getElement = driver.find_element(By.XPATH, xpath)
        if getElement.get_attribute("aria-hidden") == "false":
            #弹窗存在
            return True
        else:
            return False

    #清空输入文本框内容
    def deleteText(self,xpath):
        sleep(1)
        driver.find_element(By.XPATH, xpath).clear()
        sleep(1)
        i = 0
        while i < 22:
            driver.find_element(By.XPATH, xpath).send_keys(Keys.BACKSPACE)
            i += 1





