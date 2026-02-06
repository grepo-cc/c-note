#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import re
import requests
import env

### linker#######################################################
# 定义接口
class LinkerCode:
    def __init__(self, markdown):
        self.log = logging.getLogger(f"mkdocs.plugins.{__name__}")
        self.markdown = markdown
# 定义具体的类
class CodeGitic(LinkerCode):
    def __init__(self, markdown):
 
        super().__init__(markdown)  
        #@  gitic 的url
        #^ 
        self.git_static_url = "http://cl1157.:30001/mygitic?d="
        self.git_static_blob = "http://cl1157.:30001/mygitib?d="
        
        ##@ 判断环境是服务器版还是客户端版
    def giticfalsechange(self,stri,file_url_blbo,m,n):
          
        giticchnage =  m[0].replace(stri, "#" + stri )
        self.markdown = self.markdown.replace(
            m[0], 
            "\n" + n[1] +  "[" +  n[3] +"](" + file_url_blbo + "){.go-gitic}" + giticchnage
            )
        self.log.warning("URL is accessible" + file_url_blbo + "URL returned status code:" )
        self.log.debug("code  changed======================0" + giticchnage)
    
     
#########################################################################
#########################################################################
    #@ 修改 markdown 代码块跳转 gitic   
    ##@ ```--8<-- "@gitic:/```
    ##@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def giticedit(self):
        # --@-- [start:]	
        
        #@ 正则 key string
        regm = r'(\s*?)```([\s\S]*?)(\r?\n|(?<!\n)\r)([\s\S]*?)```'
        pattern = re.compile(regm)
        
        #@ 将匹配到的字符串进行分组， 
        #^ a.1
        #^ a.2
        #^ a.3
        #^ a.4 
        for m in re.finditer(pattern, self.markdown): 
            stri = '--8<-- "@gitic:/'
            if m[4].find(stri)>=0 :
                for mi, mv in m.groupdict():
                    self.log.debug("```code```=====================@" + mi, mv) 
                #@ 正则 key string
                regm = r'([\s\S]*?)(--8<--\ \"\@gitic\:)([\s\S]*?)(\")'
                pattern = re.compile(regm)
                
                #@ 将匹配到的字符串进行分组， 
                #^ a.0
                #^ a.1 
                #^ a.2
                #^ a.3 -为 -8<-- "@gitic:/ 后的 url
                #^ a.4
                for n in re.finditer(pattern, m[4]):   
                    for mi, mv in enumerate(n):
                        self.log.debug("giticedit=====================@" + mi, mv)  
                  
                    #@ 客户端使用工厂类创建对象,判断链接是否可以正常访问
                    mkenv_c = env.EnvProcessor().order(env.EnvGitic(etype=0,rreq={ 'check_url' : self.git_static_blob + n[3]}))
                    Rcheck_state = mkenv_c.Rcheck_state
                    if(Rcheck_state):
                        self.markdown = self.markdown.replace("\"@gitic:", "\"" + self.git_static_url )                               
                    else:
                        self.giticfalsechange(stri,file_url_blbo,m,n)

################################################
# 定义依赖注入
#^ 调用代码
# processor = LinkerCodePro()
# processor.order({},)
class LinkerCodePro:
    def order(self,linker):
        linker.giticedit()
        return linker


