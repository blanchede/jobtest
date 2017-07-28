#!/user/bin/env python
# -*-coding:utf-8-*-

#from publicMethod import login
import public.publicMethod
from public.publicMethod import CommonMethod
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddGroup(unittest.TestCase):

    def setUp(self):
        self.driver = public.publicMethod.driver
        self.targetGroupName = public.publicMethod.targetGroupName
        self.folderName = public.publicMethod.folderName
        self.editTargetName = public.publicMethod.newTargetGroupName
        self.editFolderName = public.publicMethod.newFolderName
        # XPath
        self.contactXpath = public.publicMethod.contactXpath
        self.inputTargetNameXpath = "//input[@data-uat-key='contact-group-name']"
        self.targetGroupSaveXpath = "//app-contact-group-create/nz-popup//nz-btn"
        self.vertifyTargetXpath = "//a[@title='%s']/i[@class='fa fa-list']" % self.targetGroupName
        self.vertifyEditTargetXpath = "//a[@title='%s']/i[@class='fa fa-list']" % self.editTargetName
        self.cancelEditGroupXpath = "//app-contact-group-create/nz-popup//button"
        self.vertifyEditFolderXpath = "//a[@title='folder %s']" % self.editFolderName
        self.verifyToFolderXpath = "//a[@title='folder %s']/parent::div/following-sibling::ul//a[@title='%s']" % (
            self.folderName, self.editTargetName)
        # 删除固定的组
        self.deleteTargetXpath = "//a[@title='%s']/following-sibling::div/nz-toolbar/div" % self.targetGroupName
        # 新增目标组或文件夹按钮
        self.addGroupXpath = "//nz-btn[@data-uat-key='create-contact-group']/div"
        # 右侧弹出编辑
        self.clickEditXpath = "//bs-tooltip-container/div//span/i[@class='fa fa-edit']"
        # 右侧弹框删除
        self.clickDeleteXpath = "//bs-tooltip-container/div//span/i[@class='fa fa-trash-o']"
        # 右侧弹框添加到文件夹
        self.clickLoopXpath = "//bs-tooltip-container/div//span/i[@class='ti-loop']"
        # 右侧弹框向上移动
        self.clickUpXpath = "//bs-tooltip-container/div//span/i[@class='fa fa-arrow-up']"
        # 右侧弹框向下移动
        self.clickDownXpath = "//bs-tooltip-container/div//span/i[@class='fa fa-arrow-down']"
        # 确认删除按钮
        self.comfirDeleteXpath = "//div[@aria-hidden='false']//nz-btn/div[@class='UiBtn layout-text color-ok']"


    '''# 登录
    def test_login(self):
        driver = self.driver
        driver.get(public.publicMethod.testUrl)
        driver.find_element(By.NAME, 'email').send_keys(public.publicMethod.userName)
        driver.find_element(By.NAME,'password').send_keys(public.publicMethod.password)
    #设置隐式等待为3秒
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,public.publicMethod.loginXpath).click()'''



    def test_addTarget(self):
        # 新建目标组
        selectTargetGroupXpath = "/html/body/app-root/app-layout/div/section/ng-component/app-contact-group-create/nz-popup/div/div/div/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]"


        driver = self.driver
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.contactXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.addGroupXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, selectTargetGroupXpath).click()
        sleep(2)
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.inputTargetNameXpath).send_keys(self.targetGroupName)
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.targetGroupSaveXpath).click()
         #验证新增目标组成功
        sleep(3)

        if CommonMethod.isElementExist(self.vertifyTargetXpath):
            print("目标组:%s新增成功,结果为success" % self.targetGroupName)
        else:
            print("目标组:%s新增失败，结果为success" % self.targetGroupName)
        #添加截图，定位问题，后续添加

    #删除新建目标组，测试过程中需要
    '''
    driver.find_element(By.XPATH,deleteTargetXpath).click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,clickDeleteXpath).click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH,comfirDeleteXpath).click()
    '''



    #编辑目标组
    def test_editTargetGroup(self):
        # Xpath
        # 编辑固定目标组
        editTargetXpath = "//a[@title='%s']/following-sibling::div/nz-toolbar/div" % self.targetGroupName

        driver = self.driver
        driver.find_element(By.XPATH,editTargetXpath).click()
        driver.find_element(By.XPATH,self.clickEditXpath).click()
         #取消编辑
        sleep(1)
        driver.find_element(By.XPATH,self.cancelEditGroupXpath).click()
        sleep(1)
        if CommonMethod.isElementExist(self.vertifyTargetXpath):
            print("目标组:%s未被修改，结果为success" % self.targetGroupName)
        else:
            print("目标组:%s被修改，结果为fail" % self.targetGroupName)

        driver.find_element(By.XPATH, editTargetXpath).click()
        driver.find_element(By.XPATH, self.clickEditXpath).click()
        sleep(1)
        driver.find_element(By.XPATH, self.inputTargetNameXpath).clear()
        driver.find_element(By.XPATH, self.inputTargetNameXpath).send_keys(self.editTargetName)
        driver.find_element(By.XPATH, self.targetGroupSaveXpath).click()
        sleep(1)
        if CommonMethod.isElementExist(self.vertifyEditTargetXpath):
            print("目标组修改为:%s，结果为success" % self.editTargetName)
        else:
            print("目标组:%s修改失败,结果为fail" % self.targetGroupName)



    #将目标组添加到文件夹
    def test_loopTarget(self):
        # Xpath
        # 选定固定目标组
        selectTargetXpath = "//a[@title='%s']/following-sibling::div/nz-toolbar/div" % self.editTargetName
        cancelLoopTargetXpath = "//nz-add-to-folder/nz-popup//button"
        selectToFolderXpath = "//nz-add-to-folder/nz-popup//nz-select//button"
        # 选择添加到固定文件夹
        clickToFolderXpath = "//nz-add-to-folder/nz-popup//a[@title='%s']" % self.folderName
        saveToFolderXpath = "//nz-add-to-folder/nz-popup//nz-btn"

        driver = self.driver
        driver.find_element(By.XPATH, selectTargetXpath).click()
        driver.find_element(By.XPATH, self.clickLoopXpath).click()
        # 取消添加到文件夹
        sleep(1)
        driver.find_element(By.XPATH, cancelLoopTargetXpath).click()
        sleep(1)
        #验证并未添加到某个组--目标组仍被查询到，未被放入文件夹
        if CommonMethod.isElementExist(self.vertifyEditTargetXpath):
            print("目标组:%s未被加入文件夹，结果为success"%self.editTargetName)
        else:
            print("目标组:%s被加入文件夹,结果为fail"%self.editTargetName)
        #添加到文件夹folderName
        driver.find_element(By.XPATH,selectTargetXpath).click()
        driver.find_element(By.XPATH,self.clickLoopXpath).click()
        driver.find_element(By.XPATH,selectToFolderXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH,clickToFolderXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH,saveToFolderXpath).click()
        sleep(1)
        #验证添加到folderName文件夹--根据folderName文件夹查找XPath元素成功
        driver.find_element(By.XPATH,"//a[@title='folder %s']"%self.folderName).click()
        driver.implicitly_wait(2)
        if CommonMethod.isElementExist(self.verifyToFolderXpath):
            print("目标组:%s成功加入文件夹，结果为success"%self.editTargetName)
        else:
            print("目标组:%s未添加入文件夹,结果为fail"%self.editTargetName)




    #新建文件夹
    def test_addFolder(self):
        selectFolderXpath = "/html/body/app-root/app-layout/div/section/ng-component/app-contact-group-create/nz-popup/div/div/div/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]"
        vertifyFolderXpath = "//a[@title='folder %s']/i[@class='fa fa-folder']" % self.folderName
        # 删除固定的文件夹 XPath
        deleteFolderXpath = "//a[@title='folder %s']/following-sibling::div/nz-toolbar/div" % self.folderName
        driver = self.driver
        sleep(2)
        driver.find_element(By.XPATH, self.addGroupXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, selectFolderXpath).click()
        sleep(2)
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, self.inputTargetNameXpath).send_keys(self.folderName)
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.targetGroupSaveXpath).click()
        # 验证新增文件夹成功
        sleep(3)

        if CommonMethod.isElementExist(vertifyFolderXpath):
            print("文件夹:%s新增成功" % self.folderName)
        else:
            print("文件夹:%s新增失败" % self.folderName)
        # 添加截图，定位问题，后续添加

    #删除文件夹，测试过程中需要
    '''
    driver.find_element(By.XPATH, deleteFolderXpath).click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, clickDeleteXpath).click()
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, comfirDeleteXpath).click()
    '''





    #编辑文件夹
    def test_editFolder(self):
        editFolderXpath = "//a[@title='folder %s']/following-sibling::div/nz-toolbar/div" % self.folderName
        vertifyFolderXpath2 = "//a[@title='folder %s']" % self.folderName

        driver = self.driver
        driver.find_element(By.XPATH, editFolderXpath).click()
        driver.find_element(By.XPATH, self.clickEditXpath).click()
        #取消编辑
        sleep(1)
        driver.find_element(By.XPATH,self.cancelEditGroupXpath).click()
        sleep(2)
        #取消编辑验证
        if CommonMethod.isElementExist(vertifyFolderXpath2):
            print("文件夹:%s取消编辑成功,结果为success" % self.folderName)
        else:
            print("文件夹:%s被编辑，取消编辑失败，结果为fail" % self.folderName)
        #编辑文件夹名，成功
        driver.find_element(By.XPATH, editFolderXpath).click()
        driver.find_element(By.XPATH, self.clickEditXpath).click()
        sleep(1)
        driver.find_element(By.XPATH, self.inputTargetNameXpath).clear()
        sleep(2)
        driver.find_element(By.XPATH, self.inputTargetNameXpath).send_keys(self.editFolderName)
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.targetGroupSaveXpath).click()
        #验证编辑文件夹成功
        if CommonMethod.isElementExist(self.vertifyEditFolderXpath):
            print("文件夹名:%s编辑为%s,结果为success" % (self.folderName,self.editFolderName))
        else:
            print("文件夹名:%s编辑失败，结果为fail" % self.folderName)


    #删除文件夹和目标组
    def test_deleteGroup(self):
        newFolderXpath = "//a[@title='folder %s']/following-sibling::div/nz-toolbar/div" % self.editFolderName
        confirmDeleteFolderXpath = "//div[@aria-hidden='false']//nz-btn/div[@class='UiBtn layout-text color-ok']"
        deleteNewTargetXpath = "//a[@title='folder %s']/parent::div/following-sibling::ul//a[@title='%s']/following-sibling::div" % (self.editFolderName, self.editTargetName)
        verifyInFolderXpath = "//a[@title='folder %s']/parent::div/following-sibling::ul//a[@title='%s']" % (self.editFolderName, self.editTargetName)

        driver = self.driver
        sleep(1)
        driver.find_element(By.XPATH, newFolderXpath).click()
        driver.find_element(By.XPATH, self.clickDeleteXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, confirmDeleteFolderXpath).click()
        #里面有目标组，删除失败,校验
        sleep(1)
        if CommonMethod.isElementExist(self.vertifyEditFolderXpath):
            print("文件夹名:%s存在目标组，未被删除,结果为success" % self.editFolderName)
        else:
            print("文件夹名:%s存在目标组，删除成功，结果为fail" % self.editFolderName)
        sleep(1)
        #删除目标组
        driver.find_element(By.XPATH, "//a[@title='folder %s']" % self.editFolderName).click()
        sleep(1)
        driver.find_element(By.XPATH, deleteNewTargetXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.clickDeleteXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, self.comfirDeleteXpath).click()
        #点击文件夹，验证删除
        sleep(1)
        driver.find_element(By.XPATH, "//a[@title='folder %s']" % self.editFolderName).click()
        driver.find_element(By.XPATH, newFolderXpath).click()
        if CommonMethod.isElementExist(self.verifyToFolderXpath):
            print("删除目标组：%s失败，结果为fail" % self.editTargetName)
        else:
            print("删除目标组：%s成功，结果为success" % self.editTargetName)
        #删除文件夹
        driver.find_element(By.XPATH, newFolderXpath).click()
        driver.find_element(By.XPATH, self.clickDeleteXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, confirmDeleteFolderXpath).click()
        #验证文件夹删除成功
        sleep(1)
        if CommonMethod.isElementExist(self.vertifyEditFolderXpath):
            print("文件夹名:%s不存在目标组，删除失败,结果为fail" % self.editFolderName)
        else:
            print("文件夹名:%s不存在目标组，删除成功，结果为success" % self.editFolderName)








