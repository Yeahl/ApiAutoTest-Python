# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : test_class.py  封装get、post...方法
@ide    : PyCharm
@time   : 2019-06-17 10:45:16
"""

import requests
from result.log import Logger
import time
from json import dumps

class TestClass(object):
    def __init__(self,url=None,data=None,headers=None):
        """
        :param url: 接口地址
        :param data: 传递参数
        :param headers: 请求头
        """
        self.url = url
        self.data = data
        self.headers = headers
        #获取session
        #self.session = requests.session()
        #self.session.post(self,url=url,json=data,headers=headers)

    def run_get(self,url,data,headers):
        # python用requests发送https的请求时，有安全验证，将验证设置为verify=False 即可
        # paramers 将data转换成 a=1&b=2 格式
        re = requests.get(url=url,paramers=data,headers=headers,verify=False)

        #打印状态码
        print(re.status_code)
        print(re.text)


    def run_post(self,url,data,headers):
        #json=data 将data转换成json格式
        # ce = requests.options(url=url)
        re = requests.post(url=url, json=data, headers=headers,verify=False)
        # return re.json()
        print(re.json())
        # 打印状态码
        # print(re.status_code)
        # print(re.text)

    def test_all(self,method, url, data, headers):
        """
        判断执行方法

        """
        if method == "get":
            self.run_get(url,data,headers)
        else:
            self.run_post(url,data,headers)

    def run_log(self,case_number=None,case_name=None,method=None,url=None, data=None,headers=None, code=None,asster=None,rpe=None):

        now = time.strftime("%Y-%m-%d")

        log = Logger('{}_ALL.log'.format(now), level='info')
        log.logger.info("用例编号====>{}".format(case_number))
        log.logger.info("用例标题====>{}".format(case_name))
        log.logger.info("请求方式====>{}".format(method))
        log.logger.info("请求地址====>{}".format(url))
        log.logger.info("请求头====>{}".format(dumps(headers,indent=4)))
        log.logger.info("请求参数====>{}".format(dumps(data,indent=4)))
        log.logger.info("接口响应状态码====>{}".format(code))
        log.logger.info("接口响应体为====>{}".format(rpe))



if __name__ == '__main__':
    method1 = "post"
    url1 = "http://222.198.115.85:8090/userAuth"
    data1 = ""
    headers1 = {"Content-Type":"application/json"}
    TestClass.test_all(method1,url1,data1,headers1)