import re
import scrapy
from scrapy.http import Request
from kd.items import KdItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Kd_spider(CrawlSpider):
    name = "kd"
    allowed_domains = ["kdnuggets.com"]
    start_urls = [
        "http://www.kdnuggets.com/2015/07/index.html"
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('http://www.kdnuggets.com/\d{4}/\d{2}/index.html', ), unique=True)),
        
             
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('http://www.kdnuggets.com/\d{4}/\d{2}/.*.html', )), callback='parse_item'),

    )

    

    def parse_item(self, response):

        item = KdItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@id="content"]/h1/text()').extract()
        item['text'] = response.xpath('//div[@id="post-"]/text()').extract()
        #item['html'] = response.xpath('/html').extract()

        yield item

            
    
