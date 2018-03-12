# -*- coding: utf-8 -*-
import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = []
    # start_urls = ['http://www.weibo.cn/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        post_url = 'https://passport.weibo.cn/sso/login'
        data = {
            'username': '17701256561',
            'password': 'lizhibin666',
            'savestate': '1',
            'r': '',
            'ec': '0',
            'pagerefer': 'http://weibo.cn/',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': '',
        }
        headers = {
            'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
        }
        yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.lala, headers=headers)

    def lala(self, response):
        # print(response.text)
        url = 'https://weibo.cn/6388179289/info'
        # 再次发送request请求即可
        yield scrapy.Request(url=url, callback=self.haha)

    def haha(self, response):
        with open('weibo.html', 'w', encoding='utf-8') as fp:
            fp.write(response.text)
