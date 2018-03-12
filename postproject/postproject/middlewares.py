# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class Proxy(object):
    # 重写这个方法，添加代理
    def process_request(self, request, spider):
        request.meta['proxy'] = 'https://113.68.202.10:9999'
        return None
