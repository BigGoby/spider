# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影的名字
    name = scrapy.Field()
    # 电影的简介
    movie_info = scrapy.Field()
    # 海报的链接
    image_url = scrapy.Field()
    # 剧情简介
    # story_info = scrapy.Field()
    # 下载地址
    download_url = scrapy.Field()
    
