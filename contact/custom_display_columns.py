#!/user/bin/env python
# -*-coding:utf-8-*-
#定制显示列

import public.publicMethod
import unittest
from time import sleep
import random
from selenium.webdriver.common.by import By

class TestCustomDisplayColumns(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = public.publicMethod.driver
        #定义list存放已选定制项
        self.selectList = []
        #验证可选项都存在list  ！！！！后续根据需求更改验证数组
        self.verifySelectList = ['ID', '头像', '名字', '性别', '昵称', '手机号码', '座机号码', '电子邮箱', '国家', '省',
                                  '城市', '街道', '邮编', '职位', '部门', '公司', '创建来源', '创建时间', '更新时间']

        #Xpath
        self.contactXpath = public.publicMethod.contactXpath
        self.showListXpath = "//nz-action-list/div/div"
        self.goCustomXpath = "//a[text()='定制显示列']/parent::li"
        #进入联系人界面
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, self.contactXpath).click()
        #全选、全不选。。。
        self.selectNoneXpath = "//span[text()='全不选']/parent::div"
        self.selectAllXpath = "//span[text()='全选']/parent::div"
        self.selectInvertXpath = "//span[text()='反选']/parent::div"
        self.saveXpath = "//nz-multi-choice//span[text()='保存']/parent::div"
        #可选所有项
        self.selectsXpath = "//input[@type='checkbox']"

        #定制完后页面显示项 list
        self.displayAllXpath = "//nz-list-table//th"


    #取消定制显示列
    def test_cancelCustom(self):
        #Xpath
        cancelXpath = "//nz-multi-choice//button"

        driver = self.driver
        driver.find_element(By.XPATH, self.showListXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.goCustomXpath).click()
        sleep(1)
        #验证所有可选项正确
        # 获取所有可选
        selectsSpan = driver.find_elements(By.XPATH, "//div[@class='checkbox c-checkbox']/span")
        i = 0
        #验证每个可选项text为预期值
        for selected in selectsSpan:
            self.assertEqual(selected.text,self.verifySelectList[i])
            i += 1

        driver.find_element(By.XPATH, cancelXpath).click()
        sleep(1)
        # popup Statue false:弹窗在 true：弹窗消失
        self.isPopupShow = self.driver.find_element(By.XPATH, "//nz-multi-choice/nz-popup/div").get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        if self.isPopupShow == "true" :
            print("取消定制显示列成功，结果为success")
        else:
            print("取消定制显示列失败，结果为fail")


    #全不选，定制显示列失败
    def test_selectNoneCustom(self):

        driver = self.driver
        driver.find_element(By.XPATH, self.showListXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.goCustomXpath).click()
        sleep(1)
        driver.find_element(By.XPATH, self.selectNoneXpath).click()
        driver.find_element(By.XPATH, self.saveXpath).click()
        self.isPopupShow = self.driver.find_element(By.XPATH, "//nz-multi-choice/nz-popup/div").get_attribute(
            "aria-hidden")
        print(self.isPopupShow)
        if self.isPopupShow == "false":
            print("选择至少要一列，定制显示列失败，结果为success")
        else:
            print("定制显示列成功，结果为fail")

    #全选，定制显示列成功
    def test_selectAllCustom(self):


        driver = self.driver
        driver.find_element(By.XPATH, self.selectAllXpath).click()
        driver.implicitly_wait(2)
        #获取所有可选
        selects = driver.find_elements(By.XPATH, self.selectsXpath)
        selectsSpan = driver.find_elements(By.XPATH, "//div[@class='checkbox c-checkbox']/span")
        totalNum = len(selects)
        #取出被选中的定制项
        i = 0
        for selected in selects:
            if selected.is_selected():
                    #get_attribute("ng-reflect-model") == "true":
                print("i：%d" % i)
                print("wenben:%s" %(selectsSpan[i].text) )
                #print("wenben:%s" % )
                self.selectList.append(selectsSpan[i].text)
            else:
                print("未被选中")
            i += 1

        print(self.selectList)
        #验证定制显示列成功
        self.assertEqual(totalNum,len(self.selectList),msg="全选失败")
        driver.find_element(By.XPATH, self.saveXpath).click()
        sleep(1)
        displayAll = driver.find_elements(By.XPATH, self.displayAllXpath)
        num = 0
        while num < len(self.selectList):
            self.assertEqual(self.selectList[num],displayAll[num].text,msg="验证%s定制显示失败" % self.selectList[num])
            num += 1
        print("全选定制显示列成功，结果为success")



    #随机选中部分，定制显示列成功
    def test_randomSelectCustom(self):
        driver = self.driver
        driver.find_element(By.XPATH, self.showListXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.goCustomXpath).click()
        sleep(1)
        # 获取所有可选
        selects = driver.find_elements(By.XPATH, self.selectsXpath)
        selectsSpan = driver.find_elements(By.XPATH, "//div[@class='checkbox c-checkbox']/span")
        #设置随机点击次数 定义在1到20次
        number = random.randint(1,20)
        print("随机点击次数为%d" % number)

        #进行随机点击
        i = 0
        while i < number :
            # 设置每次点击位置 根据总可选数量设置点击位置
            index = random.randint(0, (len(selects) - 1))
            #验证选中后，状态被改变
            if selects[index].is_selected() == True:
                selects[index].click()
                self.assertEqual(selects[index].is_selected(),False,msg="点击后选中状态未改变，结果为fail")
            else:
                selects[index].click()
                self.assertEqual(selects[index].is_selected(),True,msg="点击后选中状态未改变，结果为fail")
            i += 1

        #获取被选中定制项
        n = 0
        self.selectList = []
        for selected in selects:
            if selected.is_selected():
                    #get_attribute("ng-reflect-model") == "true":
                print("n：%d" % n)
                print("wenben:%s" %(selectsSpan[n].text) )
                #print("wenben:%s" % )
                self.selectList.append(selectsSpan[n].text)
            else:
                print("未被选中")
            n += 1
        print(self.selectList)
        # 验证定制显示列成功
        driver.find_element(By.XPATH, self.saveXpath).click()
        sleep(1)
        displayAll = driver.find_elements(By.XPATH, self.displayAllXpath)
        num = 0
        while num < len(self.selectList):
            self.assertEqual(self.selectList[num], displayAll[num].text, msg="随机选中，验证%s定制显示失败" % self.selectList[num])
            num += 1
        print("随机选中定制显示列成功，结果为success")


    #选中反选后，定制显示列成功
    def test_selectInvertCunstom(self):
        driver = self.driver
        #进入选择界面
        driver.find_element(By.XPATH, self.showListXpath).click()
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.goCustomXpath).click()

        #定义一个list 存放选中状态
        selectStatus = []
        # 获取所有可选
        selects = driver.find_elements(By.XPATH, self.selectsXpath)
        selectsSpan = driver.find_elements(By.XPATH, "//div[@class='checkbox c-checkbox']/span")
        i = 0
        while i < len(selects):
            #默认选中状态占位
            selectStatus.append(True)
            if selects[i].is_selected():
                selectStatus[i] = True
            else:
                selectStatus[i] = False
            i += 1

        #点击反选按钮
        driver.find_element(By.XPATH, self.selectInvertXpath).click()
        #验证反选后，之前选中的变为false，未被选中的变为True
        i = 0
        while i < len(selects):
            if selects[i].is_selected():
                selectStatus[i] = False
            else:
                selectStatus[i] = True
            i += 1

        # 获取被选中定制项
        n = 0
        self.selectList = []
        for selected in selects:
            if selected.is_selected():
                # get_attribute("ng-reflect-model") == "true":
                print("n：%d" % n)
                print("wenben:%s" % (selectsSpan[n].text))
                self.selectList.append(selectsSpan[n].text)
            else:
                print("未被选中")
            n += 1
            print(self.selectList)

        # 验证定制显示列成功
        driver.find_element(By.XPATH, self.saveXpath).click()
        sleep(1)
        displayAll = driver.find_elements(By.XPATH, self.displayAllXpath)
        num = 0
        while num < len(self.selectList):
            self.assertEqual(self.selectList[num], displayAll[num].text, msg="反选，验证%s定制显示失败" % self.selectList[num])
            num += 1
        print("反选定制显示列成功，结果为success")

    def tearDown(self):
        print("test end")







