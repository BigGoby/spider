# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request

class HuaprojectPipeline(object):
    # 重写构造方法，在这打开文件
    def __init__(self):
        # 文件的打开写到这里，仅会执行一次
        self.fp = open('xiaohua.json', 'w', encoding='utf-8')
        
    def open_spider(self, spider):
        pass

    # 在这里处理每一个item
    def process_item(self, item, spider):
        # 将这个对象转化为字典
        obj = dict(item)

        # 将图片下载到本地
        dirpath = r'C:\Users\ZBLi\Desktop\1706\day07\huaproject\huaproject\spiders\images'
        # 获取图片后缀名
        suffix = os.path.splitext(obj['image_url'])[-1]
        # 拼接文件名
        filename = obj['like'] + '_' + obj['school'] + '_' +  obj['name'] + suffix
        # 将文件路径和文件名拼接出来文件的全路径
        filepath = os.path.join(dirpath, filename)
        # 下载图片
        urllib.request.urlretrieve(obj['image_url'], filepath)

        # 将obj转化为字符串
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    # 重写这个方法，在关闭spider的时候将文件资源关闭
    def close_spider(self, spider):
        self.fp.close()
