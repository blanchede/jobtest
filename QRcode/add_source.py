#!/user/bin/env python
# -*-coding:utf-8-*-
#新建来源  !!!后续需添加联系人处来源可选已新增来源

import public.publicMethod
from public.publicMethod import CommonMethod
import unittest
import time
from time import sleep
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

#获取当前时间戳，保证建立来源和营销活动不重复
radomNum = time.time()
class TestAddSource(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = public.publicMethod.driver
        print(radomNum)
        self.testName = "test%d" % radomNum
        print(self.testName)
        #Xpath
        self.QRcodeXpath = "//a[@title='智能二维码']/parent::div"
        self.addXpath = "//app-wx-qrcode-nav//nz-btn[@data-uat-key='create-wx-qrcode-group']"
        #self.inputActivityXpath = "//app-wx-qrcode-group-create//input[@name='campaignNameField.name']"
        self.inputSourceXpath = "//app-wx-qrcode-group-create//input[@name='sourceNameField.name']"
        self.closeXpath = "//app-wx-qrcode-group-create//button"
        self.saveXpath = "//app-wx-qrcode-group-create//nz-btn/div"
        #获取膜层XPath，判断创建弹窗是否显示在界面
        self.showXpath = "//app-wx-qrcode-group-create/div"
        #self.activityEditXpath = "//a[contains(@route,'campaign') and @title='%s']/following-sibling::div" % self.testName
        self.sourceEditXpath = "//a[contains(@route,'source') and @title='%s']/following-sibling::div" % self.testName


    #创建来源
    def test_addSource(self):
        #Xpath
        clickSourceXpath = "//h3[text()='来源']/parent::div/parent::div"
        sourceFolderXpath = "//span[text()='按来源划分']/parent::a/parent::div"
        sourceStatusXpath = "//span[text()='按来源划分']/parent::a/i"

        driver = self.driver
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, self.QRcodeXpath).click()
        driver.find_element(By.XPATH, self.addXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, clickSourceXpath)

        #点击关闭设置窗口，取消创建来源成功
        sleep(1)
        driver.find_element(By.XPATH, self.closeXpath).click()
        sleep(1)
        # popup Statue false:弹窗在 true：弹窗消失
        self.isPopupShow = self.driver.find_element(By.XPATH, self.showXpath).get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        self.assertEqual(self.isPopupShow,"true","取消创建来源失败，结果为fail")
        print("test1_点击关闭创建窗口，取消创建来源成功--success")

        #文本为空，创建来源失败，提示不能为空
        driver.find_element(By.XPATH, self.addXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, clickSourceXpath)
        driver.find_element(By.XPATH, self.saveXpath)
        self.isPopupShow = self.driver.find_element(By.XPATH, self.showXpath).get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        self.assertEqual(self.isPopupShow, "false", "新建创建来源失败，结果为fail")
        print("test2_文本为空，创建来源失败，提示不能为空--success")

        #创建营销活动成功
        sleep(1)
        driver.find_element(By.XPATH, self.inputSourceXpath).send_keys(self.testName)
        driver.find_element(By.XPATH, self.saveXpath).click()
        sourceFolderStatus = driver.find_element(By.XPATH, sourceStatusXpath).get_attribute("class")
        #创建成功后验证
        sleep(1)
        if sourceFolderStatus == "fa fa-folder":
            #判断文件夹为关闭状态，点击打开
            driver.find_element(By.XPATH, sourceFolderXpath).click()
        else:
            print("来源文件夹已打开，不做任何操作")

        self.assertEqual(CommonMethod.is_element_present(self, self.sourceEditXpath), True, msg = "未找到新建来源，新建来源失败，结果为fail")
        print("test3_新建来源成功--success")

    #编辑来源
    def test_editSource(self):
        self.newSourceName = "test%d" % time.time()
        newSourceEditXpath = "//a[contains(@route,'source') and @title='%s']/following-sibling::div" % self.newSourceName
        print(self.newSourceName)
        driver = self.driver
        #取消编辑
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, self.sourceEditXpath).click()
        sleep(1)
        driver.find_element(By.XPATH, self.closeXpath).click()
        sleep(1)
        #验证取消编辑成功
        self.isPopupShow = self.driver.find_element(By.XPATH, self.showXpath).get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        self.assertEqual(self.isPopupShow, "true", "取消编辑来源失败，结果为fail")
        self.assertEqual(CommonMethod.is_element_present(self, self.sourceEditXpath), True, msg="未找到来源，编辑来源失败，结果为fail")
        print("test4_取消编辑成功--success")

        #编辑来源名为空，保存编辑失败
        driver.find_element(By.XPATH, self.sourceEditXpath).click()
        sleep(1)
        #driver.find_element(By.XPATH, self.inputSourceXpath).clear()
        #sleep(1)
        driver.implicitly_wait(3)
        i = 0
        while i < 20:
            driver.find_element(By.XPATH, self.inputSourceXpath).send_keys(Keys.BACKSPACE)
            i += 1
        sleep(1)
        driver.find_element(By.XPATH, self.saveXpath).click()
        sleep(1)
        self.isPopupShow = self.driver.find_element(By.XPATH, self.showXpath).get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        self.assertEqual(self.isPopupShow, "false", "编辑为空，编辑创建来源成功，结果为fail")
        print("test5_文本为空，编辑来源失败，提示不能为空--success")

        #编辑来源成功
        sleep(1)
        driver.find_element(By.XPATH, self.inputSourceXpath).clear()
        sleep(1)
        driver.find_element(By.XPATH, self.inputSourceXpath).send_keys(self.newSourceName)
        driver.find_element(By.XPATH, self.saveXpath).click()
        #验证编辑成功
        sleep(1)
        print(self.sourceEditXpath)
        self.assertNotEqual(CommonMethod.is_element_present(self, self.sourceEditXpath), True, msg="编辑来源失败，之前来源名仍存在，结果为fail")
        self.assertEqual(CommonMethod.is_element_present(self, newSourceEditXpath), True, msg="编辑来源失败，未找到新来源名，结果为fail" )
        print("test6_编辑来源成功--success")

    def tearDown(self):
        print("test end")















