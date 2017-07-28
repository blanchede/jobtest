#!/user/bin/env python
# -*-coding:utf-8-*-
#数据库连接和操作公用

import pymysql
import string

class OperateMysql():
    def ConectMysql(self):
        self.db = pymysql.connect(host="106.14.139.106", user="root", password="root", database="linkflow_test",
                             charset='utf8')
    def QuerySql(self, sqlSearch):
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            selectSql = "select * from contact where (mobile_phone like '%%%s%%') or (company like '%%%s%%')" \
                        " or (email like '%%%s%%') or (name like '%%%s%%')" % (
                        sqlSearch, sqlSearch, sqlSearch, sqlSearch)
            cursor.execute(selectSql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results


        except:
            print
            "Error: unable to fecth data"

        # 关闭数据库连接
        self.db.close()

    #验证数据库搜索的数据是否都含输入text
    def is_equel_sqlselect(self,searchData,searchText):
        if searchText == "":
            print("搜索文本为空，所有数据被搜索到")
            return True
        else:
            for lisdata in searchData:
                if str(lisdata[7]).find(str(searchText)) == -1:
                    return True  # 查找公司名成功
                elif str(lisdata[12]).find(str(searchText)) == -1:
                    return True  # 查找邮箱名成功
                elif str(lisdata[18]).find(str(searchText)) == -1:
                    print("查询手机号成功")
                    return True  # 查找手机号成功
                elif str(lisdata[19]).find(str(searchText)) == -1:
                    print("查询姓名成功")
                    return True  # 查找姓名成功
                else:
                    print("未查询到")
                    return False

    #删除数据库某条信息
    def deleteFromSql(self,deleteTab,deleteId):
        cursor = self.db.cursor()
        try:
            # 执行SQL语句
            deleteSql = "DELETE FROM %s WHERE %s" % (deleteTab,deleteId)
            print(deleteSql)
            cursor.execute(deleteSql)
            self.db.commit()
            print("Delete success")
            #results = cursor.fetchall()
            #return results

        except:
            print
            "Error: unable to delet data"

        # 关闭数据库连接
        self.db.close()




