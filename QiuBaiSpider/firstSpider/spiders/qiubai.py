# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # parse函数就是文件解析函数，response就是响应对象
    def parse(self, response):
    	# with open('qiubai.html', 'w', encoding='utf-8') as fp:
    	# 	fp.write(response.text)
    	div_list = response.xpath('//div[starts-with(@id, "qiushi_tag_")]')
    	# print(type(div_list[0]))
    	# 遍历上面的列表，依次找到你所想要的内容
    	items = []
    	for div in div_list:
    		# 获取图像链接  要先通过extract转化为unicode字符串类型，在获取里面的指定内容
    		# 将内容首先保存到字典中
    		item = {}
    		image_url = div.xpath('./div[@class="author clearfix"]//img/@src').extract()[0]
    		name = div.xpath('./div[@class="author clearfix"]//img/@alt').extract()[0]
    		# age = div.xpath('./div[@class="author clearfix"]/div/text()').extract()[0]
    		age = div.xpath('./div[@class="author clearfix"]/div/text()').extract_first()
    		content = div.xpath('./a/div[@class="content"]/span/text()').extract()[0]
    		haha_count = div.xpath('./div[@class="stats"]/span/i[@class="number"]/text()').extract()[0]
    		item = {
    			'image_url': image_url,
    			'name': name,
    			'age': age,
    			'content': content,
    			'haha_count': haha_count,
    		}
    		# 将数据都保存到列表中
    		items.append(item)
    	return items

        
