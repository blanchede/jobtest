#!/user/bin/env python
# -*-coding:utf-8-*-
#新建营销活动

import public.publicMethod
from public.publicMethod import CommonMethod
import unittest
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#获取当前时间戳，保证建立来源和营销活动不重复
radomNum = time.time()

class TestAddActivity(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = public.publicMethod.driver
        print(radomNum)
        self.testName = "test%d" % radomNum
        print(self.testName)
        # Xpath
        self.QRcodeXpath = "//a[@title='智能二维码']/parent::div"
        self.addXpath = "//app-wx-qrcode-nav//nz-btn[@data-uat-key='create-wx-qrcode-group']"
        self.inputActivityXpath = "//app-wx-qrcode-group-create//input[@name='campaignNameField.name']"
        self.inputSourceXpath = "//app-wx-qrcode-group-create//input[@name='sourceNameField.name']"
        self.closeXpath = "//app-wx-qrcode-group-create//button"
        self.saveXpath = "//app-wx-qrcode-group-create//nz-btn/div"
        # 获取膜层XPath，判断创建弹窗是否显示在界面
        self.showXpath = "//app-wx-qrcode-group-create/div"
        self.activityEditXpath = "//a[contains(@route,'campaign') and @title='%s']/following-sibling::div" % self.testName

    #新建营销活动
    def test_addActivity(self):
        #Xpath
        clickSourceXpath = "//h3[text()='来源']/parent::div/parent::div"
        clickActivityXpath = "//h3[text()='营销活动']/parent::div/parent::div"
        activityFolderXpath = "//span[text()='按营销活动划分']/parent::a/parent::div"
        activityStatusXpath = "//span[text()='按营销活动划分']/parent::a/i"

        driver = self.driver
        #test需要
        #driver.implicitly_wait(2)
        #driver.find_element(By.XPATH, self.QRcodeXpath).click()
        #文本超过20，新建营销活动失败
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, self.addXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, clickSourceXpath)
        sleep(1)
        driver.find_element(By.XPATH, self.inputSourceXpath).send_keys("test12345")
        driver.find_element(By.XPATH, clickActivityXpath).click()
        sleep(1)
        driver.find_element(By.XPATH, self.inputActivityXpath).send_keys("1234567890qwertyuiop1")
        sleep(1)
        driver.find_element(By.XPATH, self.saveXpath).click()
        #验证新建营销活动失败
        self.isPopupShow = self.driver.find_element(By.XPATH, self.showXpath).get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        self.assertEqual(self.isPopupShow, "false", "新建营销活动失败，结果为fail")
        print("当文本超过20，新建营销活动失败--success")

        sleep(1)
        #新建营销活动成功
        i = 0
        while i < 21:
            driver.find_element(By.XPATH, self.inputActivityXpath).send_keys(Keys.BACKSPACE)
            i += 1
        sleep(1)
        driver.find_element(By.XPATH, self.inputActivityXpath).send_keys(self.testName)
        driver.find_element(By.XPATH, self.saveXpath).click()
        sleep(1)
        #验证新建营销活动成功
        activityFolderStatus = driver.find_element(By.XPATH, activityStatusXpath).get_attribute("class")
        if activityFolderStatus == "fa fa-folder":
            #判断文件夹为关闭状态，点击打开
            driver.find_element(By.XPATH, activityFolderXpath).click()
        else:
            print("营销活动文件夹已打开，不做任何操作")
        self.assertEqual(CommonMethod.is_element_present(self, self.activityEditXpath), True, msg = "未找到新建营销活动，新建营销活动失败，结果为fail")
        print("test2_新建营销活动成功--success")

    #编辑营销活动
    def test_editActivity(self):
        self.newActivityName = "test%d" % time.time()
        newActivityEditXpath = "//a[contains(@route,'campaign') and @title='%s']/following-sibling::div" % self.newActivityName
        print(self.newActivityName)
        driver = self.driver

        #不编辑活动，未做修改编辑营销活动成功
        driver.find_element(By.XPATH, self.activityEditXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, self.saveXpath).click()
        #验证保存后，营销活动名未被改变，编辑成功
        sleep(1)
        self.assertEqual(CommonMethod.is_element_present(self, self.activityEditXpath), True, msg="不修改信息，编辑营销活动失败，结果为fail")
        print("test3_对信息不做修改,编辑营销活动成功--success")

        #修改营销活动名后保存，编辑营销活动成功
        driver.find_element(By.XPATH, self.activityEditXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, self.inputActivityXpath).clear()
        sleep(1)
        driver.find_element(By.XPATH, self.inputActivityXpath).send_keys(self.newActivityName)
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.saveXpath).click()
        #验证编辑营销活动成功
        sleep(1)
        self.assertNotEqual(CommonMethod.is_element_present(self, self.activityEditXpath), True, msg="被编辑营销活动名，编辑营销活动失败，结果为fail")
        self.assertEqual(CommonMethod.is_element_present(self, newActivityEditXpath), True, msg="修改信息，编辑营销活动失败，结果为fail")
        print("test4_编辑营销活动成功--success")









