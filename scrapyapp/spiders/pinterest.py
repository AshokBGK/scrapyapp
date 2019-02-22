# -*- coding: utf-8 -*-
import scrapy


class PinterestSpider(scrapy.Spider):
    name = 'pinterest'
    allowed_domains = ['pinterest.com']
    start_urls = ['https://tr.pinterest.com/']

    def parse(self, response):
        sources_list = self.getSourcesList()
        print '#'*100

    def getSourcesList(self):
        sources = []
        try:
            sources = [
                'bestlouboutinshop.com',
                'pesbuy.com',
                'SabiaConcept.com',
                'stilterzi.com'
            ]
        except:
            pass
        return sources

