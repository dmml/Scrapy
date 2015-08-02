import re
import scrapy
import requests
from scrapy.http import Request
from datasc.items import DatascItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector


class Datasc_spider(CrawlSpider):
    name = "datasc"
    allowed_domains = ["datasciencecentral.com"]
    start_urls = [
        "http://www.datasciencecentral.com/profiles/blog/list"
    ]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('http://www.datasciencecentral.com/profiles/blog/list\?page=\d+',), unique=True)),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('http://www.datasciencecentral.com/profiles/blogs/.*',)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = DatascItem()
        item['url'] = response.url
        item['title'] = response.xpath('//div[@class="tb"]/h1/text()').extract()
        item['author'] = response.xpath('//div[@class="tb"]/ul/li/a[2]/text()').extract()
        item['text'] = response.xpath('//div[@class="postbody"]/div[@class="xg_user_generated"]/p/text()').extract()
        item['date'] = response.xpath('//div[@class="tb"]/ul/li/a[3]/text()').extract()

        yield item
