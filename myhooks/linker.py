#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import re
import requests
import env


# 定义接口
class Rezemble:
    def __init__(self):
        self.github_io_cnote = "https://grepo-cc.github.io/c-note/"
    
    def findfile(self):
        pass

# 定义具体的类
class RezembleLocal(Rezemble):

    def findfile(self,linx):
        
        types = ["jpg","svg","png","gif","pdf"]
        images = "assets/images/"
        docs =  "./docs/"
        isox = linx
        for ctype in types:
            filepath = images + linx +"."+ctype
            
            # 指定的文件或目录存在
            if os.path.isfile(docs + filepath): 
                # self.markdownurlreplace(alt_str,filepath,m)
                 isox = self.github_io_cnote + filepath
        return   isox   

# 定义具体的类
class HfileLocal(Rezemble):

    def findfile(self,linx):
        filepath = "http://cl1157.:30001/hfile/" + linx + ""
        return   filepath   

# 定义具体的类
#$ 修改指定代号路径 
#@ ![](@net/数据传输控制方式.svg) 
#！ 作废
class Fnet(Rezemble):
    def findfile(self,linx):
        return   self.github_io_cnote + "asset/net/"

'''
 # 定义工厂类
class RezembleFactory:
    def create_factory(self, Ftype,  **kwargs):
        if Ftype == 'local':
            return RezembleLocal( **kwargs)
        elif Ftype == 'hfile':
             return HfileLocal( **kwargs)
        else:
            raise ValueError(f'Unknown shape type: {env_type}')
'''

# 定义依赖注入
class RezembleProcessor:
    # def __init__(self,rezemble):
    #     self.rezemble = rezemble
    def order(self,linx,rezemble):
        return rezemble.findfile(linx)
#x 依赖注入使用方法
# local_service = RezembleLocal()
# processor = RezembleProcessor()
# processor.order(linx,local_service)
##########################################################
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
        #! 使用相对路径 访问域名需注意 https://WW.io.com/ALERT
        #! github pages 的 路径 https://grepo-cc.github.io/c-note/blog/archive/2024/c-note/assets/images/2af993c759774e1385abcbdd70f4cb8b.
        self.images = "https://grepo-cc.github.io/c-note/assets/images/"

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
                    # Cnote =  {check_url = "https://grepo-cc.github.io/c-note/"}
                    factory = env.EnvFactory()
                    mkenv_c = factory.create_factory('gitic',etype=0, rreq={check_url : self.git_static_blob + n[3]} )
                    Rcheck_state = mkenv_c.Rcheck_state
                    if(Rcheck_state):
                        self.markdown = self.markdown.replace("\"@gitic:", "\"" + self.git_static_url )                               
                    else:
                        self.giticfalsechange(stri,file_url_blbo,m,n)
 
 
#########################################################################
    #@ hfilelinker
    # ![](@img:hfile/2)
    # @img:/hfile/2
    def hfileload(self):
   
        stri = '\@hfile-'
        # self.regx(stri,'hfile')
        self.regx(stri,HfileLocal())
 
#########################################################################
    #$ 修改本地文件代码   
    #@ ![](:/6d7af8c2ca774d5399b974b88c2bace1)
    #@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def localfile(self):
  
        #@ 正则key string
        stri = ':/'        
        # regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        # pattern = re.compile(regm)
      
        # self.regx(stri,"local") #工厂方法
        self.regx(stri,RezembleLocal())
       
   
    #@ regcomm
    # ![](@img:hfile/2)
    # @img:/hfile/2
    def regx(self,stri,Rezemblename):
  
        # factory = RezembleFactory() #工厂方法
        processor = RezembleProcessor() #依赖注入
      
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)
        #@ 将匹配到的字符串进行分组， 
        #^ a.1 为 [] 内字符串
        #^ a.2 为 （ 和 正则 key string
        #^ a.3 为 () 内文件索引
        #^ a.4 为 ）
        for m in re.finditer(pattern, self.markdown):   
            # for mi, mv in m.groupdict():
            #     self.log.debug("hfileload=====================@" + mi, mv)  
            #@ alt_str href 
            alt_str =  m[1] if len(m[1]) > 0  else ""
            
            #@ 准备替换的文字
            oldxstri = "![" + m[1] +"]" +m[2]+ m[3] +  m[4]+ ""

            # Rezemble = factory.create_factory(Rezemblename)
            # filepath = Rezemble.findfile(m[3])

            filepath = processor.order(m[3],Rezemble)
            # newstri = "![" + m[1] +"]" + "(" + filepath + ")" + ""
            newstri = f'<center > <img \
                style="width:30%!important;height:30%!important;" \
                controls="" \
                src="{filepath}">\
                </img>  \
                <figcaption>{alt_str} </figcaption> \
                </center>'
            self.markdown = self.markdown.replace(oldxstri,newstri)

# 定义工厂类 
class LinkerFactory:
    def create_factory(self, env_type, *args):
        if env_type == 'local':
            return LinkerLocal(*args)
        elif env_type == 'gitic':
            return LinkerGitic(*args)
        else:
            raise ValueError(f'Unknown shape type: {env_type}')

#@ 客户端使用工厂类创建对象
#^ 调用代码
# factory = linker.LinkerFactory()
# linker_c = factory.create_factory('local', markdown)
# linker_c.localfile()
# linker_c.giticedit(giticheck)
# linker_c.hfileload()
	 