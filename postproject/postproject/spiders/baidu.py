# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']

    # http://fanyi.baidu.com/sug
    # start_urls = ['http://www.baidu.com/']

    # def parse(self, response):
    #     pass

    # 如果想要自己直接发送post请求，则需要重写这个方法。
    # 这个方法以前就是遍历start_urls列表，生成请求对象的
    def start_requests(self):
    	post_url = 'http://fanyi.baidu.com/sug'
    	word = 'world'
    	data = {
    		'kw': word
    	}
    	yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.parse_post)

    def parse_post(self, response):
    	print(response.text)
