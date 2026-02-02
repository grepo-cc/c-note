#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import requests

# 定义接口
class Env:
    def __init__(self, type):
        self.type = type
        self.giticheck_state = False
        self.giticheck()
        print("p~~~~~~~~ giticheck_state:",  self.giticheck_state)
       
    def initennv(self):
        pass

    ##@ 判断环境是服务器版还是客户端版
    # --@-- [start:]
    def giticheck(self):
        file_url_blbo = "192.168.120.157" 
        try:
            response = requests.get(file_url_blbo,timeout=1)
            if response.status_code == 200:
                self.giticheck_state = True
            else:
                self.giticheck_state = False
        except requests.exceptions.RequestException as e:
            print("~~~~~~~~Error:", e)
            self.giticheck_state = False
        print("~~~~~~~~Error:",  self.giticheck_state)
        # return self.giticheck_state
    # --@-- [end:]  
# 定义具体的类
class EnvLocal(Env):
    def __init__(self, type):
        super().__init__(type)
        print("~~~~~~~~ giticheck_state:",  self.giticheck_state)

    def initennv(self):
        tinydict = {'a': 1, 'b': 2, 'b': '3'}
        return tinydict

# 定义具体的类
class EnvGitic(Env):
 

    def initennv(self):
        tinydict = {'a': 1, 'b': 2, 'b': '3'}
        return tinydict

 

# 定义工厂类
class EnvFactory:
    def create_factory(self, env_type, *args):
        if env_type == 'local':
            return EnvLocal(*args)
        elif env_type == 'gitic':
            return EnvGitic(*args)
        else:
            raise ValueError(f'Unknown shape type: {env_type}')

# 客户端使用工厂类创建对象
# factory = EnvFactory()
# circle = factory.create_factory('local', 5)
# print(circle.area()) # 输出圆的面积

 