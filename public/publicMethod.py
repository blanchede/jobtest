#!/user/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

#启动chromdriver
driver = webdriver.Remote(command_executor='http://localhost:9515',
                          desired_capabilities=DesiredCapabilities.CHROME)
#测试地址
#testUrl="http://devtest.leadswarp.com"
testUrl="http://localhost:4200/"
#testUrl="http://106.14.139.106:80"

#登录需要信息
#测试用户名和密码
userName = "demo@demo.com"
password = "demo"
#登录按钮XPath
loginXpath = "/html/body/app-root/app-login/div/div/div/div[2]/form/button"
#主界面联系人按钮
contactXpath = "//li[3]/div/a/i"
#测试分组固定信息
targetGroupName = "targetGroupTest1"
folderName = "folderTest1"
newTargetGroupName = "targetGroupTest2"
newFolderName = "folderTest2"

#公用方法 元素是否存在


def isElementExist(Xpath):
    s=driver.find_elements(By.XPATH, Xpath)

    if len(s) == 0:
        print("元素未找到:%s"%Xpath)
        return  False
    elif len(s) == 1:
        return  True
    else:
        print("找到%s个元素：%s"%(len(s),Xpath))
        return False

