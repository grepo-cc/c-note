#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import requests

# 定义接口
class Env:
    def __init__(self, etype,rreq):
        self.etype = etype
        self.Rcheck_state = False

        # 检查键是否存在
        if 'check_url' in rreq:
            self.requestcheck(rreq['check_url'])
            print("p~~~~~~~~ Rcheck_state:",  self.Rcheck_state)
            print("键 'check_url' 存在于字典中")
        else:
            print("键 'check_url' 不存在于字典中")
       
    def initennv(self):
        pass

    #@ 判断环境是服务器版还是客户端版
    def requestcheck(self,check_url):
        try:
            response = requests.get(check_url,timeout=1)
            if response.status_code == 200:
                self.Rcheck_state = True
            else:
                self.Rcheck_state = False
        except requests.exceptions.RequestException as e:
            print("~~~~~~~~Error:", e)
            self.Rcheck_state = False
        print("REQUEST CHECK~~~~~~~~:",  self.Rcheck_state)
      
#####################################################################
#@ 定义具体的类1
class EnvLocal(Env):
    def __init__(self, etype,rreq):
        #@ 调用父类的 __init__ 方法 
        #! 不能加self
        super().__init__( etype,rreq)  # 调用父类的 __init__ 方法
        print("~~~~~~~~ child class init method:",  self.Rcheck_state)
    def initennv(self):
        tinydict = {'a': "local env", 'b': 2, 'b': '3'}
        return tinydict

#@ 定义具体的类2
class EnvGitic(Env):
    def initennv(self):
        tinydict = {'a': "gitic env", 'b': 2, 'b': '3'}
        return tinydict

#@ 定义具体的类3
class EnvGithub(Env):
    def __init__(self, etype,rreq):
        #@ 调整，作废
        '''
        self.etype = etype
        self.Rcheck_state = False
        self.cnote_url = "https://grepo-cc.github.io/c-note/"
        self.requestcheck(cnote_url)
        print("p~~~~~~~~ Rcheck_state:",  self.Rcheck_state)
        '''
        #@ 调用父类的 __init__ 方法 
        #! 不能加self
        super().__init__(etype,rreq)  
        print("~~~~~~~~ child class init method:",  self.Rcheck_state)
    def initennv(self):
        tinydict = {'a': "github env", 'b': 2, 'b': '3'}
        return tinydict

 ##################################################################

#@ 定义工厂类
#^ 客户端使用工厂类创建对象
""" class EnvFactory:
    def create_factory(self, env_type,  **kwargs):
        if env_type == 'local':
            return EnvLocal( **kwargs)
        elif env_type == 'gitic':
            return EnvGitic( **kwargs)
        elif env_type == 'github':
            return EnvGithub( **kwargs)
        else:
            raise ValueError(f'Unknown shape type: {env_type}') """


# 定义依赖注入
#^ 调用代码
# processor = EnvProcessor()
# processor.order({},EnvGithub(etype=0,rreq={}))
class EnvProcessor:
    def order(self,envx):
        envx.initennv()
        return envx