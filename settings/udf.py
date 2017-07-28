#!/user/bin/env python
# -*-coding:utf-8-*-
#定制显示列

import public.publicMethod
import unittest
from public.elementOperate import ElementMethod
from public.publicMethod import CommonMethod
from public.pymysqlCommon import OperateMysql
from time import sleep
from selenium.webdriver.common.by import By

clickFolderXpath = "//span[text()='自定义字段']/parent::a/parent::div"
folderXpath = "//span[text()='自定义字段']/parent::a/i"
clickContactXpath = "//span[text()='联系人']/parent::a/parent::div"
closeXpath = "//app-setting-udf-edit//button[@aria-label='Close']"
saveXpath = "//span[text()='保存']/parent::div"
inputNameXpath = "//input[@data-uat-key='udf-input']"
popupXpath = "//app-setting-udf-edit/div"
udfName = "test123"
newUdfName = "test1234"
editUdfXpath = "//div[text()='%s']/parent::td/following-sibling::td[@class='cell-operation']/div/i[1]" % udfName
newEditUdfXpath = "//div[text()='%s']/parent::td/following-sibling::td[@class='cell-operation']/div/i[1]" % newUdfName
class TestUdf(unittest.TestCase):
    def setUp(self):
        self.driver = public.publicMethod.driver
        print("test start")

    def test_addUDF(self):
        driver = self.driver
        addUdfXpath = "//nz-btn/div[@class='UiBtn layout-icon-text color-']"
        ElementMethod.clickElement(self, public.publicMethod.settingXpath)
        ElementMethod.open_Folder(self, folderXpath, clickFolderXpath)
        ElementMethod.clickElement(self, clickContactXpath)
        #取消新建自定义字段
        ElementMethod.clickElement(self, addUdfXpath)
        ElementMethod.inputText(self, inputNameXpath, "some！@#")
        ElementMethod.clickElement(self, closeXpath)
        #验证弹窗消失
        self.assertEqual(False, ElementMethod.isPopupExist(self,popupXpath), msg="弹窗未消失，取消新建自定义字段失败")
        self.assertEqual(False, CommonMethod.is_element_present(self,"//nz-list-table//div[text()='some！@#']"),
                         msg="新增udf被找到，取消新建自定义字段失败")

        #输入字符超过20位，新建自定义字段失败
        ElementMethod.clickElement(self, addUdfXpath)
        ElementMethod.inputText(self, inputNameXpath, "test12345678901234567")
        ElementMethod.clickElement(self, saveXpath)
        #验证弹窗仍然存在，新建自定义字段失败
        self.assertEqual(True, ElementMethod.isPopupExist(self, popupXpath), msg="弹窗消失--fail")

        #清除后新建自定义字段
        ElementMethod.deleteText(self, inputNameXpath)
        ElementMethod.inputText(self, inputNameXpath, udfName)
        ElementMethod.clickElement(self, saveXpath)
        #验证弹框消失，新建自定义字段显示在列表中
        self.assertEqual(False, ElementMethod.isPopupExist(self,popupXpath), msg="弹窗未消失，新建自定义字段失败--fail")
        self.assertEqual(True, CommonMethod.is_element_present(self,editUdfXpath), msg="新建自定义字段未找到，新建自定义字段失败--fail")
        #ElementMethod.clickElement(self, closeXpath)


    def test_editUDF(self):
        driver = self.driver
        ElementMethod.clickElement(self, editUdfXpath)
        ElementMethod.deleteText(self, inputNameXpath)
        ElementMethod.inputText(self, inputNameXpath, newUdfName)
        ElementMethod.clickElement(self, saveXpath)
        #验证编辑成功
        self.assertEqual(False, ElementMethod.isPopupExist(self, popupXpath), msg="弹窗未消失，编辑自定义字段失败--fail")
        self.assertEqual(True, CommonMethod.is_element_present(self, newEditUdfXpath),
                         msg="编辑自定义字段未找到，编辑自定义字段失败--fail")






    #将添加数据从数据库删除
    def test_deleteInSql(self):
        driver = self.driver
        OperateMysql.ConectMysql(self)
        OperateMysql.deleteFromSql(self,"custom_field","name='%s'"% newUdfName)
        driver.refresh()
















