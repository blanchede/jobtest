#!/user/bin/env python
# -*-coding:utf-8-*-
#根据搜索内容，搜索联系人

import unittest
from time import sleep
from selenium.webdriver.common.by import By
import public.publicMethod
from public.publicMethod import CommonMethod
from public.elementOperate import ElementMethod
import pymysql
from public.pymysqlCommon import OperateMysql
from selenium.webdriver.common.keys import Keys

searchisName = "姓名"
searchPhone = "153"
searchEmail = "9178"
searchCompany = "公司"


class TestSearchContacts(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = public.publicMethod.driver
        self.contactXpath = public.publicMethod.contactXpath
        self.searchBtnXpath = "//app-nz-search/div/div[@class='search-icon ']"
        self.inputSearchXpath = "//input[@placeholder='搜索']"



    def test_searchContacts(self):
        driver = self.driver
        testArry = [searchisName, searchPhone, searchEmail, searchCompany]
        endPageXpath = "//app-pagination//span[text()='末页']/parent::button"
        nextPageXpath = "//app-pagination//span[text()='下页']/parent::button"
        firstPageXpath = "//app-pagination//span[text()='首页']/parent::button"
        #Xpath
        searchNumXpath = "//nz-list-table//tbody/tr"
        ElementMethod.clickElement(self, self.contactXpath)

        for searchName in testArry:
            print("jsdh")
            print(searchName)
            i = 0
            while i < 20:
                driver.find_element(By.XPATH, self.inputSearchXpath).send_keys(Keys.BACKSPACE)
                i += 1
            #driver.find_element(By.XPATH, self.inputSearchXpath).clear()
            ElementMethod.inputText(self, self.inputSearchXpath, searchName)
            ElementMethod.clickElement(self, self.searchBtnXpath)

            #查询数据库
            OperateMysql.ConectMysql(self)
            searchData = OperateMysql.QuerySql(self, searchName)
            #print("searchData:" )
            #print(searchData)
            #print("row%s" % len(searchData))
            #将查询数据与数据库作对比
            if len(searchData ) < 21:
                # 获取查询后页面元素
                searchElements = driver.find_elements(By.XPATH, searchNumXpath)
                self.assertEqual(len(searchData), len(searchElements), msg="查询数据与搜索数据不一致，结果为fail")
                self.assertEqual(True, OperateMysql.is_equel_sqlselect(self, searchData, searchName),
                                 msg="数据库查询数据未含搜索文本，结果fail")
                #页面显示数据校验 第一种：用所有text对比
                for element in searchElements:
                    self.assertEqual(str(searchName) in element.text,True,msg="页面数据不包含查询文本")
                #第二种 指定显示数据对比（只用名字、电话号码等可搜索数据对比）!!!未写


            else:
                #点击首页
                ElementMethod.clickElement(self, firstPageXpath)
                # 获取查询后页面元素
                searchElements = driver.find_elements(By.XPATH, searchNumXpath)
                for element in searchElements:
                    self.assertEqual(str(searchName) in element.text, True, msg="页面数据不包含查询文本")
                searchNum = len(searchElements)
                while driver.find_element(By.XPATH,nextPageXpath).is_enabled() == True:
                    ElementMethod.clickElement(self, nextPageXpath)
                    searchElements = driver.find_elements(By.XPATH, searchNumXpath)
                    for element in searchElements:
                        self.assertEqual(str(searchName) in element.text, True, msg="页面数据不包含查询文本")
                    searchNum += len(searchElements)
                    sleep(1)
                self.assertEqual(len(searchData), searchNum, msg="查询数据与搜索数据不一致，结果为fail")
                self.assertEqual(True, OperateMysql.is_equel_sqlselect(self, searchData, searchName),
                                 msg="数据库查询数据未含搜索文本，结果fail")








