# -*- coding: utf-8 -*-
import scrapy
from movieproject.items import MovieprojectItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
    	# 找到所有的电影
        table_list = response.xpath('//div[@class="co_content8"]/ul//table')
        # 遍历所有的电影列表，得到电影的详细信息
        for table in table_list:
        	# 在当前的页面的只能提取到两个信息，一个是name，一个是movie_info
        	# 创建一个对象
        	item = MovieprojectItem()
        	# 提取对应的信息  
        	# 【注】在点的后面要加两个杠
        	item['name'] = table.xpath('.//a[@class="ulink"]/text()').extract_first()
        	item['movie_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
        	# 获取电影的链接
        	movie_url = 'http://www.dytt8.net' + table.xpath('.//a[@class="ulink"]/@href').extract_first()
        	# yield item

        	# 这里面涉及到一个传递item的问题，我们要学习如何传参,加上一个meta参数，meta参数是一个字典，过去之后，通过字典的键获取其值
        	yield scrapy.Request(url=movie_url, callback=self.parse_info, meta={'item': item})

    # 获取item的其它信息
    def parse_info(self, response):
    	# 获取到传递过来的参数
    	item = response.meta['item']
    	# 接着解析网页，获取item的其它信息
    	item['image_url'] = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
    	# item['story_info'] = response.xpath('')
    	item['download_url'] = response.xpath('//td[@bgcolor="#fdfddf"]/a/text()').extract_first()

    	yield item

