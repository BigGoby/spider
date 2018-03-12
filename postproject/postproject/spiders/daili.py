# -*- coding: utf-8 -*-
import scrapy


class DailiSpider(scrapy.Spider):
    name = 'daili'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?ie=UTF-8&wd=ip']

    def parse(self, response):
        with open('ipdaili.html', 'w', encoding='utf-8') as fp:
        	fp.write(response.text)
