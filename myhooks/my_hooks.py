import logging,mkdocs.plugins
import re
import os.path
import time
import env,conf,linker
# import ruamel.yaml

### log加载
log = logging.getLogger(f"mkdocs.plugins.{__name__}")
# 客户端使用工厂类创建对象
""" factory = env.EnvFactory()
mkenv_c = factory.create_factory('local',etype=0,rreq={})
mkenv_dic = mkenv_c.initennv()
Rcheck_state = mkenv_c.Rcheck_state """

processor = env.EnvProcessor()
envx1 = processor.order(env.EnvLocal(etype=0,rreq={}))

processor2 = env.EnvProcessor()
envx2 = processor2.order(env.EnvGithub(etype=0,rreq={check_url : "https://github.com/"}))

log.warning("env local ======================" +str(envx1.Rcheck_state))
log.warning("env local ======================" +str(envx1.mkenv_dic))

log.warning("env github ======================" +str(envx2.Rcheck_state))
log.warning("env github ======================" +str(envx2.mkenv_dic))
	

def on_startup(command,dirty ):

	print("on_startup=======================")
	# factory = conf.ConfFactory()
	# conf_c = factory.create_factory('auto',"")
	# conf_c.autoconf('')
	
def on_config(config, **kwargs):
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
 

	# exit()
 
	#依赖注入	
	processor = linker.LinkerProcessor()
	linker_c = processor.order(linker.LinkerLocal(markdown))
	markdown = linker_c.markdown

	#@ debug 文件名
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

	