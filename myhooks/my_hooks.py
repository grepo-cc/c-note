import logging,mkdocs.plugins
import re
 
import os.path

import time
import env,conf,linker
# import ruamel.yaml




### log加载
log = logging.getLogger(f"mkdocs.plugins.{__name__}")

# 客户端使用工厂类创建对象
factory = env.EnvFactory()
mkenv_c = factory.create_factory('local',etype=0,rreq={})
mkenv_dic = mkenv_c.initennv()
Rcheck_state = mkenv_c.Rcheck_state
 



def on_startup(command,dirty ):

	print("on_startup=======================")

	# factory = conf.ConfFactory()
	# conf_c = factory.create_factory('auto',"")
	# conf_c.autoconf('')
	
def on_config(config, **kwargs):

	log.warning("env ======================" +str(Rcheck_state))
	log.warning("env ======================" +str(mkenv_dic))
	
	# exit()
	# os.abort()
	# 客户端使用工厂类创建对象
	factory = conf.ConfFactory()
	conf_c = factory.create_factory('auto',"")
	conf_c.autoconf("config")
	print(config)
	 
	# config['theme']['name']='material'
	# config['site_url']='material'

	return config
	
# def on_pre_build( config):
# 	log.warning("on_pre_build======================" )

def on_page_markdown(markdown,page,config, **kwargs):
	print(config)

	# exit()
	#客户端使用工厂类创建对象
	# factory = linker.LinkerFactory()
	# linker_c = factory.create_factory('local', markdown)
	# linker_c.localfile()
	# linker_c.giticedit()
	# linker_c.hfileload()
	

	#依赖注入	
	processor = linker.LinkerProcessor()
	linker_c = processor.order(linker.LinkerLocal(markdown))
	
	
	markdown = linker_c.markdown
	
		

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

	filed = page.file.dest_uri
	if filed.find('dockerfile')>=0:
		log.warning(filed)
		log.warning(markdown)
	
		# os.abort()
	return markdown
# def on_page_content(html ,page ,config ,files):
# 	factory = conf.ConfFactory()
# 	conf_c = factory.create_factory('auto',"")
# 	conf_c.autoconf("config")
# 	config = print(config)
 
# 	return html
# return markdown.replace('a','fff')

	