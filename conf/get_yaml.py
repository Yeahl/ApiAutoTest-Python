# coding:utf-8
"""
@project : jiekou
@author  : 三十
@file   : get_yaml.py 读取配置文件
@ide    : PyCharm
@time   : 2019-06-17 15:45:16
"""


import yaml
import os
def GetYaml():

    # 获取当前文件路径
    filePath = os.path.dirname(__file__)
    #print(filePath)
    # 获取当前文件的Realpath
    fileNamePath = os.path.split(os.path.realpath(__file__))[0]
    #print(fileNamePath)
    # 获取配置文件的路径
    yamlPath = os.path.join(fileNamePath,'conf.yaml')
    #print(yamlPath)
    # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
    f = open(yamlPath,mode='r',encoding='utf-8')

    cont = f.read()
    #Loader=yaml.FullLoader屏蔽yaml.load警告
    x = yaml.load(cont,Loader=yaml.FullLoader)
    #获取测试环境ip
    ip = x["test_ip"]["ip"]
    # 获取线上环境ip
    #ip = x["online_ip"]["ip"]
    #print(ip)
    # 关闭文件
    f.close()
    return ip

#GetYaml()
