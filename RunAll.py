# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : RunAll.py 执行程序
@ide    : PyCharm
@time   : 2019-06-17 15:45:16
"""

from common import test_class
from conf import config_operate


if __name__ == "__main__":
    # mothod = "get"
    # url = "http://www.baidu.com"
    # data = {}
    a = config_operate.Conf()
    a.conf()
    mothod = "post"
    dz = "/api/subject/academicCooperation/findAcademicCooperation"
    url = ip+dz
    data = {"data": {
		"name": "",
		"cooperationUnit": "",
		"personInCharge": ""
	},
	"page": 1,
	"size": 200}
    #将data转换成json
    # data = json.dumps(data)
    # print(data)
    headers = {"Content-Type":"application/json"}
    r = test_class.TestClass()
    r.test_all(mothod,url,data,headers)







    #引用 pytest 输出测试报告
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")
    #
    # pytest.main(['-s', './common/test_class.py', '--html=report/{}_report.html'.format(now)])
