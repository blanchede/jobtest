#!/user/bin/env python
# -*-coding:utf-8-*-

#from publicMethod import login
import public.publicMethod
import unittest
from time import sleep
from assertpy import assert_that
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestAddContact(unittest.TestCase):
    def setUp(self):
        print("test start")
        self.driver = public.publicMethod.driver
        # XPath
        self.contactXpath = public.publicMethod.contactXpath
        self.addContactXpath = "/html/body/app-root/app-layout/div/section/ng-component/div/div[2]/ng-component/div/div[1]/div[2]/div[2]/nz-btn"
        self.nameXpath = "//div[@data-uat-key='name']/div/div/input"
        self.nicknameXpath = "//div[@data-uat-key='nickname']/div/div/input"
        self.sexXpath = "//div[@data-uat-key='gender']/div/div/nz-select/div"
        self.sexXpath1 = "//a[@title='保密']"
        self.sexXpath2 = "//a[@title='男']"
        self.sexXpath3 = "//a[@title='女']"
        self.phoneXpath = "//div[@data-uat-key='mobilePhone']/div/div/input"
        self.homePhoneXpath = "//div[@data-uat-key='homePhone']/div/div/input"
        self.emailXpath = "//div[@data-uat-key='email']/div/div/input"
        self.countryXpath = "//div[@data-uat-key='country']/div/div/input"
        # 省
        self.stateXpath = "//div[@data-uat-key='state']/div/div/input"
        self.cityXpath = "//div[@data-uat-key='city']/div/div/input"
        self.streetXpath = "//div[@data-uat-key='street']/div/div/input"
        # 邮编
        self.postalCodeXpath = "//div[@data-uat-key='postalCode']/div/div/input"
        # 行业
        self.industryXpath = "//div[@data-uat-key='industry']/div/div/input"
        self.companyXpath = "//div[@data-uat-key='company']/div/div/input"
        # 部门
        self.departmentXpath = "//div[@data-uat-key='department']/div/div/input"
        # 职位
        self.positionXpath = "//div[@data-uat-key='title']/div/div/input"
        self.websiteXpath = "//div[@data-uat-key='website']/div/div/input"
        self.addSourceXpath = "//div[@data-uat-key='source']/div/div/nz-select/div"
        self.sourceXpath1 = "//a[@title='-- 无 --']"
        # 备注
        self.commentsXpath = "//div[@data-uat-key='comments']/div/div/textarea"
        # 保存按钮
        self.saveXpath = "//nz-btn[@data-uat-key='contact-save']/div"
        # 取消按钮
        self.cancelXpath = "//nz-btn[@data-uat-key='contact-cancel']/div"

    # 登录
    def test_login(self):
        driver = self.driver
        driver.get(public.publicMethod.testUrl)
        driver.find_element(By.NAME, 'email').send_keys(public.publicMethod.userName)
        driver.find_element(By.NAME,'password').send_keys(public.publicMethod.password)
        #设置隐式等待为3秒
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,public.publicMethod.loginXpath).click()

    #联系人
    def test_goContact(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,self.contactXpath).click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(self.addContactXpath).click()

    #新建联系人
    def test_addContact(self):
        driver = self.driver
        driver.implicitly_wait(3)
        #名字不输入，提示名字不能为空
        #driver.find_element(By.XPATH,saveXpath).click()
        # #assert_that(driver.switchTo().alert().getText()).is_equal_to("名字是必填字段,不能为空")
        #assert_that(driver.find_element(By.TAG_NAME("body")).getText().contains("名字是必填字段,不能为空")).is_true()
        driver.find_element(By.XPATH, self.nameXpath).send_keys('姓名')
        driver.find_element(By.XPATH,self.nicknameXpath).send_keys('昵称')
        driver.find_element(By.XPATH,self.sexXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH,self.sexXpath3).click()
        driver.find_element(By.XPATH,self.phoneXpath).send_keys("15320855177")
        driver.find_element(By.XPATH,self.homePhoneXpath).send_keys("023-72162051")
        driver.find_element(By.XPATH,self.emailXpath).send_keys("917805067@qq.com")
        driver.find_element(By.XPATH,self.countryXpath).send_keys("中国")
        driver.find_element(By.XPATH,self.stateXpath).send_keys("江苏省")
        driver.find_element(By.XPATH,self.cityXpath).send_keys("南京市")
        driver.find_element(By.XPATH,self.streetXpath).send_keys("铁西街道")
        driver.find_element(By.XPATH,self.postalCodeXpath).send_keys("4001003")
        driver.find_element(By.XPATH,self.industryXpath).send_keys("互联网行业")
        driver.find_element(By.XPATH,self.companyXpath).send_keys("某公司")
        driver.find_element(By.XPATH,self.departmentXpath).send_keys("研发部门")
        driver.find_element(By.XPATH,self.positionXpath).send_keys("web开发")
        driver.find_element(By.XPATH,self.websiteXpath).send_keys("www.baidu.com")
        driver.find_element(By.XPATH,self.addSourceXpath).click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH,self.sourceXpath1).click()
        driver.find_element(By.XPATH,self.commentsXpath).send_keys("备注某事")
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH,self.saveXpath).click()

    #联系人添加后信息比对（后续添加），添加到目标组
    def test_contactInfoVerify(self):
        print("信息比对，后面添加")




    #将联系人，添加和取消关联到目标组
    def test_addAndDeleteConnectionGroup(self):
        # 添加到目标组按钮
        addGroupXpath = "//div[@class='group-item']/span/i"
        addGroupXpath2 = "/html/body/app-root/app-layout/div/section/ng-component/div/div[2]/app-contact-detail/div/div[2]/div[1]/div[2]/ul/li[15]/div[2]/div/div/span/i"
        selectGroupXpath = "//nz-select[@class='full']/div/button"
        # 根据设置目标组，修改选择的title名
        selectGroupXpath1 = "//a[@title='eqweqwe']"
        addGroupSaveXpath = "//nz-btn[@data-uat-key='save']/div"
        addGroupCancelXpath = "/html/body/app-root/app-layout/div/section/ng-component/div/div[2]/app-contact-detail/nz-add-to-group/nz-popup/div/div/div/div[1]/button"
        addGroupDeleteXpath = "//div[@class='group-item']/span/i[@class='fa fa-trash']"

        driver = self.driver
        driver.find_element(By.XPATH,addGroupXpath).click()
        #取消添加到目标组
        #driver.implicitly_wait(3)
        driver.find_element(By.XPATH,addGroupCancelXpath).click()
        #确认目标组未添加（后续添加）
        sleep(3)
        driver.find_element(By.XPATH,addGroupXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,selectGroupXpath).click()
        driver.implicitly_wait(3)
        #选定分组
        sleep(1)
        driver.find_element(By.XPATH,selectGroupXpath1).click()
        driver.find_element(By.XPATH,addGroupSaveXpath).click()
        #确认目标组已添加（后续添加）
        #删除关联目标分组
        sleep(3)
        driver.find_element(By.XPATH,addGroupDeleteXpath).click()
        #确认目标组关联已取消（后续添加）



    #确保以上按钮，点击跳转有效
    def test_other(self):
        # 返回联系人列表按钮
        backContactListXpath = "//nz-btn[@data-uat-key='back-contact-list']/div"
        # 编辑联系人按钮
        editContactXpath = "//nz-btn[@data-uat-key='update-contact']/div"
        verifyLabelXpath = "//div[@class='left-panel']/span[text()='编辑联系人']"

        driver = self.driver
        driver.find_element(By.XPATH,editContactXpath).click()
        driver.implicitly_wait(3)
        #确认跳转到编辑联系人界面
        assert_that(driver.find_element(By.XPATH,verifyLabelXpath).text).is_equal_to("编辑联系人")
        driver.find_element(By.XPATH,self.cancelXpath).click()
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH,backContactListXpath).click()
        #确认返回联系人列表
        assert_that(driver.find_element(By.XPATH,"//div[@class='left-panel']/span[text()='所有联系人']"))
        #driver.quit()

    def tearDown(self):
        #self.driver.quit()
        print("test end")


if __name__ == '__main__':
    #构造测试集
    '''suit = unittest.TestSuite()
    suit.addTest(TestAddContact("test_login"))
    suit.addTest(TestAddContact("test_goContact"))
    suit.addTest(TestAddContact("test_addContact"))
    suit.addTest(TestAddContact("test_contactInfoVerify"))
    suit.addTest(TestAddContact("test_addAndDeleteConnectionGroup"))
    suit.addTest(TestAddContact("test_other"))
    #执行测试
    #runner = unittest.TextTestRunner()
    #runner.run(suit)'''
