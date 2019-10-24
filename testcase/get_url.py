# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : get_url.py  拼接url
@ide    : PyCharm
@time   : 2019-06-17 10:45:16
"""


from testcase import get_excel
from common.test_class import *
from conf import get_yaml
import paramunittest
import unittest



config_xls = get_excel.configExcel()
# print(config_xls)

@paramunittest.parametrized(*config_xls) # 循环读取 Excel里面的数据
class GetUrl(unittest.TestCase):

    def setParameters(self,case_number,case_name,method,path, data,headers, asster):
        self.case_number = int(case_number)
        #print(self.case_number)
        self.case_name = case_name
        self.method = method
        self.path = path
        # eval()函数将字符串转换成字典，不然会报错
        self.data = eval(data)
        self.headers = eval(headers)
        self.asster = int(asster)

    def setUp(self):
        print('----------------',self.case_name+'测试开始','----------------')

    def test_case01(self): # 传入参数
        ip = get_yaml.GetYaml()
        url = ip+self.path
        #print(self.case_number,self.case_name,self.method,url,self.data,self.headers,self.asster)
        r = TestClass()
        rpe = r.test_all(self.method,url,self.data,self.headers)
        print(rpe)
        r.run_log(self.case_number,self.case_name,self.method,url,self.data,self.headers,self.asster,rpe)

    def tearDown(self):
        print()
        print('----------------',self.case_name+'测试结束','----------------')


if __name__ == '__main__':
    unittest.main().test_case01()

