# coding:utf-8

"""
@project : jiekou
@author  : 三十
@file   : config_operata.py 读取配置文件
@ide    : PyCharm
@time   : 2019-06-17 15:45:16
"""

from configparser import ConfigParser
class Conf:
    def conf(self):
        #初始化类
        cp = ConfigParser()
        cp.read("conf.cfg")

        #得到所有的section，以列表的形式返回
        section = cp.sections()[1]
        print(section)
        ip = cp.get(section,"ip")
        print(ip)
        return ip

        #得到该section的所有option
        #print(cp.options(section))

        #得到该section的所有键值对
        #print(cp.items(section))

        #得到该section中的option的值，返回为string类型
        #print(cp.get(section, "ip"))


if __name__ == '__main__':
    a=Conf()
    b = a.conf()
