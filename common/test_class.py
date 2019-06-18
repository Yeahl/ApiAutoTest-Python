# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : test_class.py  封装get、post...方法
@ide    : PyCharm
@time   : 2019-06-17 10:45:16
"""

import requests

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
        re = requests.post(url=url, json=data, headers=headers,verify=False)
        print(re.response)
        # 打印状态码
        print(re.status_code)
        print(re.text)

    def test_all(self,mothod,url,data,headers):
        """
        判断执行方法

        """
        if mothod == "get":
            self.run_get(url,data,headers)
        else:
            self.run_post(url,data,headers)



