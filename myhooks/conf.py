#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import defaultdict
import logging,mkdocs.plugins
import re
import yaml

# 定义接口
class ConfInit:
    def initennv(self):
        pass

# 定义具体的类
class ConfAuto(ConfInit):
    def __init__(self,config):
        ### log加载
        self.log = logging.getLogger(f"mkdocs.plugins.{__name__}")
        # self.mkdocs = mkdocs
        self.config = config
        self.conf_path = "/root/mysite/myhooks/conf_yamls/"
        self.doc_root = "/root/mysite/"
        # pass

    def autoconf(self,config):
        log = self.log
        # mkdocs = self.mkdocs
        # config = self.config

        log.warning("autoconf>>>>>======================" )
        #修改监控
        # config['config_file_path'] = "/root/mysite/auto.yml"
        #加载配置文件
        # load = mkdocs.config.load_config("auto.yml")
        # new_config = mkdocs.commands.build.build(load)
        # mkdocs.livereload.LiveReloadServer()
        # print( globals())

      

        # 使用示例
        ##@ 合并yaml配置文件
        files_to_merge = [
            'base.yml'
            ,'ot.yml'    
            ,'blog.yml'    
            ,'social.yml'    
            ,'git.yml'    
            ,'tag.yml'    
            ,'nav.yml'    
            ,'ex_toc.yml'    
            ,'ex_admonition.yml'    
            ,'ex_annotations.yml'    
            ,'ex_code.yml'    
            ,'ex_content.yml'    
            ,'ex_tooltips.yml'    
            ,'plugins_search.yml'    
            ,'theme_palette.yml'    
            ,'theme_font.yml'
             ]
        refresh = self.conf_path + 'refresh.yml'
     
        # 打开文件并读取内容
        ## 使用保存两次来触发修改
        with open(refresh, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
        if( content ==  'mkdocs.yml'):
            outfile = "auto.yml"
        else:
            outfile =  'mkdocs.yml'

        # 打开文件进行覆盖写
        with open(refresh ,'w') as f:
            f.write(outfile) # 写入新的内容
        # exit()
        # outfile =  'mkdocs.yml'
        output_file = self.doc_root + outfile
        self.merge_yaml_files(files_to_merge, output_file)


        # mkdocs.config.base.load_config(config_file="/root/mysite/auto.yaml")

        # config = mkdocs.config.base.load_config(config_file= output_file)
      
        # config =  mkdocs.config.load_config(output_file)
          # new_config = mkdocs.commands.serve.builder(load)

        #加载配置文件
        # config = mkdocs.config.load_config(output_file)
        # mkdocs.commands.build.build(config)
        # mkdocs.livereload.LiveReloadServer()

        # config = mkdocs.config.base.Config.load_file(config,open(output_file, 'r', encoding="utf-8"))
        # config = mkdocs.config.base.Config(output_file)

     
        # time.sleep(2 )
        return config
 
    def load_yaml_file(self,file_path):
        """加载YAML文件并返回内容"""
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)

    def merge_dicts(self,dict1, dict2):
        result = dict1.copy()
        for key, value in dict2.items():
            if key in result:
                print("key--------------")
                print(key)
                print("value-------------- ")
                print(value)
                print(type(value))
                if isinstance(value, dict):
                    result[key] = self.merge_dicts(result[key], value)
                    print("not exsit ======= back 2")
                elif isinstance(value, list):
                    result[key] = value + result[key]
                else:
                    result[key] ={  value , result[key]}   # 自定义处理逻辑，这里将值相加
            else:
                print("not exsit =======")
                result[key] = value 
                print(result)
        return result



    def merge_yaml_files(self,files, output_file):
        """合并多个YAML文件到一个文件"""
        merged_data = {}
    
        for file in files:
            file_data = self.load_yaml_file(self.conf_path + file)
           


            print(file_data)
            print("合并 文件名：：：：：：")
            print(file)
            merged_data = self.merge_dicts(merged_data, file_data)
            print("合并后的yaml config 参数：：：：：：")
            print(merged_data)

        with open(output_file, 'w') as file:
            yaml.dump(merged_data, file, default_flow_style=False)

    def saveconf(self):

        
        #
 
        # MkDocsConfig.load_file(config,file)
    
        # config_files = ["katex","theme_palette"]#"mkdocs",
        # config_kes = ["extra_javascript","extra_css","theme"]
        # for config_file in config_files:
        # 	file = open(config_file+".yml", 'r', encoding="utf-8")
        # 	file_data = file.read()
        # 	data = yaml.load(file_data,Loader=yaml.FullLoader)
        # 	# data = mkdocs.utils.yaml.yaml_load(file_data,Loader=yaml.FullLoader)
        # 	file.close()
        # 	print(data)
        # 	for config_ke in config_kes:
        # 		if ( (config_ke in config.keys()) and (config_ke in data.keys()  )):        # 			config[config_ke] = config[config_ke]+data[config_ke]
	
        
      
        
        pass
 
        # return config

# 定义工厂类
class ConfFactory:
    def create_factory(self, env_type, *args):
        if env_type == 'auto':
            return ConfAuto(*args)
        elif env_type == '1':
            return ConfAuto(*args)
        else:
            raise ValueError(f'Unknown shape type: {env_type}')
        
