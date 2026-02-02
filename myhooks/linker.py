#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging,mkdocs.plugins
import os
import re
import requests

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
        self.types = ["jpg","svg","png"]
        self.markdown = markdown
        self.git_static = "http://code160:30001/mygitic?d="
        self.git_static_blob = "http://cl1157:30001/mygitib?d="
        self.hfilelinker =  "http://cl1157:30001/hfile/"
    



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

    # --@-- [end:]  

    #@ 修改本地文件代码   
    ##@ ![](:/6d7af8c2ca774d5399b974b88c2bace1)
    ##@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def localfile(self):
        
        # markdown = self.markdown 
	# --@-- [start:]
  
        
        stri = ':/'
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)
        for m in re.finditer(pattern, self.markdown):   
            self.log.debug("LinkerLocal======================" + m[1])	
            self.log.debug("LinkerLocal======================" + m[2])	
            self.log.debug("LinkerLocal======================" + m[3])	
            self.log.debug("LinkerLocal======================" + m[4]) 
            alt_str = ""
            if len(m[1]) == 0 :
                alt_str = m[1]
            for type in self.types:
                filepath = "/assets/images/" + m[3]+"."+type
                self.log.debug(filepath) 
                # 指定的文件或目录存在
                if os.path.isfile("/root/mysite/docs"+filepath): 
                    self.markdown = self.markdown.replace(
                    "![" + alt_str +"]" +m[2]+ m[3] +  m[4]+ "",
                    "![" + alt_str +"](" + filepath  +  m[4]
                    )
                    #+ "{align=left}"
    
        # --@-- [end:]	


        ##@ 网络工程文件路径
        #--@-- [start:]

        static_url_157 = "http://cl1157:15780/myftppicgo/mksvg.php"
        static_net_url = static_url_157 + "?d=网络工程&h="

        stri = '@net/'
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)
        for m in re.finditer(pattern, self.markdown): 
            self.log.warning("net======================" + m[1])	
            self.log.warning("net======================" + m[2])	
            self.log.warning("net======================" + m[3])	
            self.log.warning("net======================" + m[4])
            self.log.warning("![" + m[1] +"]" +m[2]+ m[3] +  m[4]+ "")
            alt_str = ""
            if len(m[1]) == 0 :
                alt_str = m[1]
            if (m[2] == "("+stri) :
                self.markdown = self.markdown.replace(
                    "![" + alt_str +"]" +m[2]+ m[3] +  m[4]+ "",
                    "![" + alt_str +"](" + static_net_url+ m[3] +  m[4])#+ "{align=left}"
            # markdown = markdown.replace("(" +stri, "(" + static_net_url)
        # --@-- [end:]

        return self
    
    #@ 修改 markdown 代码块跳转 gitic   
    ##@ ```   ```
    ##@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def giticedit(self,giticheck_state):
        # --@-- [start:]	
        # giticheck_state = self.giticheck()
        stri = '--8<-- "@gitic:/'
        regm = r'(\s*?)```([\s\S]*?)(\r?\n|(?<!\n)\r)([\s\S]*?)```'
        pattern = re.compile(regm)
        for m in re.finditer(pattern, self.markdown): 
            if m[4].find(stri)>=0 :
                regm = r'([\s\S]*?)(--8<--\ \"\@gitic\:)([\s\S]*?)(\")'
                pattern = re.compile(regm)
                for n in re.finditer(pattern, m[4]):   
                    self.log.warning("giticedit======================0" + n[0])
                    self.log.warning("giticedit======================1" + n[1])
                    self.log.warning("giticedit======================2" + n[2])
                    self.log.warning("giticedit======================3" + n[3])
                    self.log.warning("giticedit======================4" + n[4])
                    # self.markdown = self.markdown.replace(m[0],  "\n" + n[1] + "[" +  n[3] +"](" + self.git_static_blob + n[3] + ")\n       " + m[0])


                    ##@ 判断环境是服务器版还是客户端版
                    # --@-- [start:]
                    file_url_blbo = self.git_static_blob + n[3] 
                    if(giticheck_state):
                        try:
                            response = requests.get(file_url_blbo,timeout=1)
                            if response.status_code == 200:
                                self.markdown = self.markdown.replace("\"@gitic:", "\"" + self.git_static )
                                # giticchnage =  m[0]
                            else:
                               self.giticfalsechange(stri,file_url_blbo,m,n)
                        except requests.exceptions.RequestException as e:
                            print("~~~~~~~~Error:", e)
                    else:
                        self.giticfalsechange(stri,file_url_blbo,m,n)
                    # --@-- [end:]    
                   
            self.log.debug("code======================0" + m[0])
            self.log.debug("code======================1" + m[1])
            self.log.debug("code======================2" + m[2])
            self.log.debug("code======================3" + m[3])
            self.log.debug("code======================4" + m[4])
	# --@-- [end:]	
        # return self
     	# --@-- [start:]	
        # ![](@img:hfile/2)
        # @img:/hfile/2
    def hfileload(self):
   
        stri = '@hfile-'
        regm = r'!\[([\s\S]*?)\](\(' + stri + ')([\s\S]*?)(\))'
        pattern = re.compile(regm)
        for m in re.finditer(pattern, self.markdown):   
            self.log.debug("hfileload======================" + m[1])	
            self.log.debug("hfileload======================" + m[2])	
            self.log.debug("hfileload======================" + m[3])	
            self.log.debug("hfileload======================" + m[4]) 
            alt_str = ""
            if len(m[1]) > 0 :
                alt_str = m[1]
    
            filepath = self.hfilelinker + m[3]
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
		# markdown = markdown.replace(oldxstri,"")
	 
   
	# --@-- [end:]	

# 定义具体的类
class LinkerGitic(Linker):
    def __init__(self, type):
        self.type = type

    def initennv(self):
        tinydict = {'a': 1, 'b': 2, 'b': '3'}
        return tinydict

 

# 定义工厂类
class LinkerFactory:
    def create_factory(self, env_type, *args):
        if env_type == 'local':
            return LinkerLocal(*args)
        elif env_type == 'gitic':
            return LinkerGitic(*args)
        else:
            raise ValueError(f'Unknown shape type: {env_type}')

# 客户端使用工厂类创建对象
# factory = LinkerFactory()
# circle = factory.create_factory('local', 5)
# print(circle.area()) # 输出圆的面积

 