# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class KdItem(scrapy.Item):
    
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    html = scrapy.Field()
    
