import unittest
#加载测试文件
from contact.add_contact_success import TestAddContact
from contact.add_group_success import TestAddGroup
from contact.custom_display_columns import TestCustomDisplayColumns

#构造添加联系人测试集
addContactSuit = unittest.TestSuite()
addContactSuit.addTest(TestAddContact("test_login"))
addContactSuit.addTest(TestAddContact("test_goContact"))
addContactSuit.addTest(TestAddContact("test_addContact"))
addContactSuit.addTest(TestAddContact("test_contactInfoVerify"))
addContactSuit.addTest(TestAddContact("test_addAndDeleteConnectionGroup"))
addContactSuit.addTest(TestAddContact("test_other"))

#构造添加分组测试集
addGroupSuit = unittest.TestSuite()
#addGroupSuit.addTest(TestAddContact("test_login"))
addGroupSuit.addTest(TestAddGroup("test_addTarget"))#新建目标组
addGroupSuit.addTest(TestAddGroup("test_editTargetGroup"))#编辑目标组 1.取消编辑 2.编辑成功
addGroupSuit.addTest(TestAddGroup("test_addFolder"))#新建文件夹
addGroupSuit.addTest(TestAddGroup("test_loopTarget"))#将目标组添加到文件夹
addGroupSuit.addTest(TestAddGroup("test_editFolder"))#编辑文件夹 1.取消编辑 2.编辑成功
addGroupSuit.addTest(TestAddGroup("test_deleteGroup"))#删除目标组和文件夹 1.文件夹含有目标组，删除失败 2.删除目标组成功 3.删除文件夹成功

#定制显示列
customDispalyColumnsSuit = unittest.TestSuite()
customDispalyColumnsSuit.addTest(TestAddContact("test_login"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_cancelCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectNoneCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectAllCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_randomSelectCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectInvertCunstom"))

# 执行测试
runner = unittest.TextTestRunner()
#runner.run(addContactSuit)
#runner.run(addGroupSuit)
runner.run(customDispalyColumnsSuit)
