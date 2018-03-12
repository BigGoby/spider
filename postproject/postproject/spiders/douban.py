# -*- coding: utf-8 -*-
import scrapy
import urllib.request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']

    def parse(self, response):
        # 去查找有没有验证码
        # 【注】如果找不到，那么返回None
        image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        # print('*'*50)
        # print(image_url)
        # print('*'*50)
        # exit()
        # 如果没有验证码图片，image_url就是None
        if not image_url:
            data = {
                'source': '',
                'redir': 'https://www.douban.com',
                'form_email': '1090509990@qq.com',
                'form_password': 'lizhibin666',
                'login': '登录',
            }
        else:
            # 获取验证码id
            captcha_id = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
            # 保存验证码图片，并且提示用户输入验证码
            urllib.request.urlretrieve(image_url, './douban.png')
            yanzhengma = input('请输入验证码:')
            data = {
                'source': '',
                'redir': 'https://www.douban.com',
                'form_email': '1090509990@qq.com',
                'form_password': 'lizhibin666',
                'captcha-solution': yanzhengma,
                'captcha-id': captcha_id,
                'login': '登录',
            }
        post_url = 'https://accounts.douban.com/login'
        yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.hehe)

    def hehe(self, response):
        # with open('douban.html', 'wb') as fp:
        #   fp.write(response.body)
        url = 'https://www.douban.com/accounts/'
        yield scrapy.Request(url=url, callback=self.dongguan)

    def dongguan(sef, response):
        with open('dong.html', 'wb') as fp:
            fp.write(response.body)
