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

        #! 部署前根据环境修改该熟悉
        self.loaalasset = self.github_io_cnote
    def findfile(self):
        pass

# 定义具体的类
class RezembleLocal(Rezemble):

    def findfile(self,linx):

         #@ 定义 localfile 方法中所需要遍历的 后缀名
        #^ 待完善、补充
        types = ["jpg","svg","png","gif","pdf"]

        #@ 全局assets images 路径
        #! 使用相对路径 访问域名需注意 https://WW.io.com/ALERT 
        #! github pages 的 路径 https://grepo-cc.github.io/c-note/blog/archive/2024/c-note/assets/images/2af993c759774e1385abcbdd70f4cb8b.
        images = "assets/images/"        
        docs =  "./docs/"

        isox = linx
        for ctype in types:
            filepath = images + linx +"."+ctype
            # 指定的文件或目录存在
            if os.path.isfile(docs + filepath): 
                # self.markdownurlreplace(alt_str,filepath,m)
                 isox = self.loaalasset + filepath
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
        # "http://cl1157.:15780/myftppicgo/mksvg.php" + "?d=网络工程&h="
        return   "http://cl1157.:30001/hfile/" + "asset/net/" + linx

 

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

### linker#######################################################
# 定义接口
class LinkerImg:
    def __init__(self, markdown):
        self.log = logging.getLogger(f"mkdocs.plugins.{__name__}")
        self.markdown = markdown

# 定义具体的类
class LinkerLocal(LinkerImg):
    #@ hfilelinker
    # ![](@img:hfile/2)
    # @img:/hfile/2
    def hfileload(self):
        stri = '\(\@hfile-'
        # self.regx(stri,'hfile')
        self.regx(stri,HfileLocal())
    #@ net
    # ![](@net/2)     
    def dirnet(self):
        stri = '\(\@net\/'       
        self.regx(stri,Fnet())
 
    #$ 修改本地文件代码   
    #@ ![](:/6d7af8c2ca774d5399b974b88c2bace1)
    #@ ![](:/root/mysite/docs/assets/images/6d7af8c2ca774d5399b974b88c2bace1)
    def localfile(self):
        stri = '\(:/'        
        self.regx(stri,RezembleLocal())
       
    def regx(self,stri,Rezemblename):
  
        # factory = RezembleFactory() #工厂方法
        processor = RezembleProcessor() #依赖注入
        #() []内不允许存在空格 取消\s 匹配
        regm = r'!\[([\S]*?)\](' + stri + ')([\S]*?)(\))'
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
            alt_str =  m[1] if len(m[1]) > 0  else m[3]
            
            #@ 准备替换的文字
            oldxstri = "![" + m[1] +"]" +m[2]+ m[3] +  m[4]+ ""

            # Rezemble = factory.create_factory(Rezemblename)
            # filepath = Rezemble.findfile(m[3])

            filepath = processor.order(m[3],Rezemblename)
            # newstri = "![" + m[1] +"]" + "(" + filepath + ")" + ""
            

            newstri = f'<center > <img \
            style="width:30%!important;height:30%!important;" \
            alt="{alt_str}"\
            controls="" \
            src="{filepath}">\
            </img>  \
            <figcaption>{alt_str} </figcaption> \
            </center>'
         
            self.log.warning("REPALCE= old ====================@" + oldxstri) 
            self.log.warning("REPALCE= ########## ====================" + m[1]) 
            self.log.warning("REPALCE= ########## ====================" + m[2]) 
            self.log.warning("REPALCE= ########## ====================" + m[3]) 
            self.log.warning("REPALCE= ########## ====================" + m[4]) 
            self.log.warning("REPALCE= new ====================@" + newstri) 
            self.markdown = self.markdown.replace(oldxstri,newstri)



# 定义依赖注入
#^ 调用代码
# processor = LinkerProcessor()
# processor.order({},LinkerLocal())
class LinkerImgProcessor:
    def order(self,linker):
        linker.localfile()
    
        linker.hfileload()
        linker.dirnet()
        return linker


 

# --@-- [start:]
	# for m in re.finditer(r'(\"@jsreps\/)([\s\S]*?)(\")', markdown): 
	
	#	log.warning("jsreps======================" + m[2])
	# static_url_157 = "http://cl1157:15780/myftppicgo/mksvg.php"
	# static_net_url = static_url_157 + "?d=网络工程&h="
	# static_js_url  = static_url_157 + "?d=jsreps&h="
	# static_cssx_url  = static_url_157 + "?d=cssx&h="
	# static_bash_url  = static_url_157 + "?d=bash_in_app&h="
	# static_url_160 = "http://code160:16080"
	# markdown = markdown.replace("\"@jsreps:", "\""+static_js_url)
	# markdown = markdown.replace("\"@cssx:", "\""+static_cssx_url)
	# markdown = markdown.replace("\"@bash:", "\""+static_bash_url)
	# markdown = markdown.replace("\"@dkpose:", "\""+static_url_160)
	# markdown = markdown.replace("\"@static157:", "\""+static_url_157 + "?d=")

	# markdown = markdown.replace("(@gitic:", "("+git_static_blob )	
# --@-- [end:]	
