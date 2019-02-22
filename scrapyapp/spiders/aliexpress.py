# -*- coding: utf-8 -*-
import scrapy


class AliexpressSpider(scrapy.Spider):
    name = 'aliexpress'
    allowed_domains = ['aliexpress.com']
    start_urls = ['http://aliexpress.com/']

    def parse(self, response):
        pass
