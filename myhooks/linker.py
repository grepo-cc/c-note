#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import re
import requests
import env

# 定义接口
class Linker:
    def localfile(self):
        pass
    def giticedit(self):
        pass

# 定义具体的类
class LinkerLocal(Linker):
    def __init__(self, markdown):
        self.log = logging.getLogger(f"mkdocs.plugins.{__name__}")

        #@ 定义 localfile 方法中所需要遍历的 后缀名
        #^ 待完善、补充
        self.types = ["jpg","svg","png","gif","pdf"]

        #@ 全局assets images 路径
        self.images = "/assets/images/"

        #@ 全局python 根目录
        self.mysite = "./"

        #@ docs 根目录
        self.docs = self.mysite + "docs/"

        #@ ![@net/]() url
        #! 已作废
        self.Fnet_url = "http://cl1157.:15780/myftppicgo/mksvg.php" + "?d=网络工程&h="
        
        #@  gitic 的url
        #^ 
        self.git_static_url = "http://cl1157.:30001/mygitic?d="
        self.git_static_blob = "http://cl1157.:30001/mygitib?d="

        #@  hfile 的url 
        self.hfilelinker =  "http://cl1157.:30001/hfile/"
    
        self.markdown = markdown

#########################################################################
    ##@ 判断环境是服务器版还是客户端版
    # --@-- [start:]
    def giticfalsechange(self,stri,file_url_blbo,m,n):
          
        giticchnage =  m[0].replace(stri, "#" + stri )
        self.markdown = self.markdown.replace(
            m[0], 
            "\n" + n[1] +  "[" +  n[3] +"](" + file_url_blbo + "){.go-gitic}" + giticchnage
            )
        self.log.warning("URL is accessible" + file_url_blbo + "URL returned status code:" )
        self.log.debug("code  changed======================0" + giticchnage)
    #@ url 的替换工厂
    def markdownurlreplace(self,al_str,f_url,m):
        self.markdown = self.markdown.replace(
                    "![" + al_str +"]" +m[2]+ m[3] +  m[4]+ "",
                    "![" + al_str +"](" + f_url  +  m[4]
                    )
                    #@ 对齐方式
                    #+ "{align=left}"
        return self
#########################################################################
    #$ 修改本地文件代码   
    #@ ![](:/6d7af8c2ca774d5399b974b88c2bace1)
    #@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def localfile(self):
        # markdown = self.markdown 

        #@ 正则key string
        stri = ':/'        
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)

        #@ 将匹配到的字符串进行分组， 
        #^ a.1 为 [] 内字符串
        #^ a.2
        #^ a.3 为 () 文件索引
        #^ a.4
        for m in re.finditer(pattern, self.markdown):   
            for mi, mv in enumerate(m):
                self.log.debug("LinkerLocal=====================@" + mi, mv) 
            alt_str =  m[1] if len(m[1]) > 0  else ""
            #@ 查找文件，一次匹配
            for ctype in self.types:
                filepath = self.images + m[3]+"."+ctype
                self.log.debug(filepath) 
                # 指定的文件或目录存在
                if os.path.isfile(self.docs + filepath): 
                    self.markdownurlreplace(alt_str,filepath,m)
        return self   
#########################################################################
    #$ 修改指定代号路径 
    #@ ![](@net/数据传输控制方式.svg) 
    def assemblefile(self):
        #@ 正则 key string
        stri = '@net/'
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)

        #@ 将匹配到的字符串进行分组， 
        #^ a.1 为 [] 内字符串 @net/
        #^ a.2
        #^ a.3 为 () 文件名
        #^ a.4
        for m in re.finditer(pattern, self.markdown): 
            for mi, mv in enumerate(m):
                self.log.debug("net=====================@" + mi, mv) 
            self.log.warning("![" + m[1] +"]" +m[2]+ m[3] +  m[4]+ "")
            alt_str =  m[1] if len(m[1]) > 0  else ""
            if len(m[1]) == 0 :
                alt_str = m[1]
            if (m[2] == "("+stri) :
                self.markdownurlreplace(alt_str,self.Fnet_url + m[3] +  m[4],m)
        return self
#########################################################################
    #@ 修改 markdown 代码块跳转 gitic   
    ##@ ```--8<-- "@gitic:/```
    ##@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def giticedit(self,giticheck_state):
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
                for mi, mv in enumerate(m):
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
                    # Cnote =  {check_url = "https://grepo-cc.github.io/c-note/"}
                    factory = env.EnvFactory()
                    mkenv_c = factory.create_factory('gitic',0,{ rreq={check_url : self.git_static_blob + n[3]} })
                    Rcheck_state = mkenv_c.Rcheck_state
                    if(Rcheck_state):
                        self.markdown = self.markdown.replace("\"@gitic:", "\"" + self.git_static_url )                               
                    else:
                        self.giticfalsechange(stri,file_url_blbo,m,n)
                    ##@ 判断环境是服务器版还是客户端版
                    '''
                    file_url_blbo = 
                    if(giticheck_state):
                        try:
                            response = requests.get(file_url_blbo,timeout=1)
                            if response.status_code == 200:
                                self.markdown = self.markdown.replace("\"@gitic:", "\"" + self.git_static_url )                               
                            else:
                               self.giticfalsechange(stri,file_url_blbo,m,n)
                        except requests.exceptions.RequestException as e:
                            print("~~~~~~~~Error:", e)
                    else:
                        self.giticfalsechange(stri,file_url_blbo,m,n)
                    '''
	 #@ hfilelinker
        # ![](@img:hfile/2)
        # @img:/hfile/2
    def hfileload(self):
   
        stri = '@hfile-'
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)
        for m in re.finditer(pattern, self.markdown):   
            for mi, mv in enumerate(m):
                self.log.debug("hfileload=====================@" + mi, mv)  
            #@ alt_str href 
            alt_str =  m[1] if len(m[1]) > 0  else ""
            filepath = self.hfilelinker + m[3]
            #@ 准备替换的文字
            oldxstri = "![" + m[1] +"]" +m[2]+ m[3] +  m[4]+ ""
            newstri = f'<center > <img \
                style="width:30%!important;height:30%!important;" \
                controls="" \
                src="{filepath}">\
                </img>  \
                <figcaption>{alt_str} </figcaption> \
                </center>'
                
            self.log.debug(filepath) 
            self.log.debug(oldxstri) 
            self.markdown = self.markdown.replace(oldxstri,newstri)