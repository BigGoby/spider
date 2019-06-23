# dushuproject 

爬取了www.dushu.com网站，并吧爬取的内容写入json文件中

1.用到了CrawlSpider它的父类是Scrapy.Spider,优势在于它可以定义规则，可以根据连接提取出指定的连接
连接提取器scrapy.linkextractors.LinkExtractor()

2.scrapy shell "http://www.xxx.com/xx/xx"
 提取所有页码的链接
 正则语法 links = LinkExtractor(xxxx）
 xpath语法 links = LinkExtractor(restrict_xpaths=r'xxxx')
 css用法 links = LinkExtractor(restrict_css='.x')
 查看提取所有的链接 links.extract_links(response)
 
3.将爬取的数据存储到mysql数据库中

# movieproject
爬去了www.yytt.com网站，爬取的内容主要是电所影排行榜，主要涉及到的就是需要的内容在N不同的页面当中

# postproject
主要是利用scrapy实现模拟登录，实现了微波和豆瓣的模拟登录

# qiubaispider
爬取糗事百科的段子

# huaproject
爬取了www.xiaohua.com网站，分类下载图片等信息

