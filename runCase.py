import unittest
#加载测试文件
from contact.add_contact_success import TestAddContact
from contact.add_group_success import TestAddGroup
from contact.custom_display_columns import TestCustomDisplayColumns
from QRcode.add_source import TestAddSource
from QRcode.add_activity import TestAddActivity
from contact.search_for_contacts import TestSearchContacts
from settings.udf import TestUdf

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

#构造搜索联系人
searchContactsSuit = unittest.TestSuite()
searchContactsSuit.addTest(TestAddContact("test_login"))
searchContactsSuit.addTest(TestSearchContacts("test_searchContacts"))

#定制显示列
customDispalyColumnsSuit = unittest.TestSuite()
customDispalyColumnsSuit.addTest(TestAddContact("test_login"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_cancelCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectNoneCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectAllCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_randomSelectCustom"))
customDispalyColumnsSuit.addTest(TestCustomDisplayColumns("test_selectInvertCunstom"))

#智能二维码
QRsuit = unittest.TestSuite()
QRsuit.addTest(TestAddContact("test_login"))
QRsuit.addTest(TestAddSource("test_addSource"))
QRsuit.addTest(TestAddSource("test_editSource"))
QRsuit.addTest(TestAddActivity("test_addActivity"))
QRsuit.addTest(TestAddActivity("test_editActivity"))

#设置
SettingSuit = unittest.TestSuite()
SettingSuit.addTest(TestAddContact("test_login"))
SettingSuit.addTest(TestUdf("test_addUDF"))
SettingSuit.addTest(TestUdf("test_editUDF"))
SettingSuit.addTest(TestUdf("test_deleteInSql"))


# 执行测试
runner = unittest.TextTestRunner()
#runner.run(addContactSuit)
#runner.run(addGroupSuit)
#runner.run(searchContactsSuit)
#runner.run(customDispalyColumnsSuit)
#runner.run(QRsuit)
runner.run(SettingSuit)

