# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuaprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片链接
    image_url = scrapy.Field()
    # 名字
    name = scrapy.Field()
    # 大学
    school = scrapy.Field()
    # 喜欢
    like = scrapy.Field()
