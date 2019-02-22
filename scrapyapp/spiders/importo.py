# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor


class ImportoSpider(scrapy.Spider):
    name = 'importo'
    # allowed_domains = ['shop.importo.eu']
    start_urls = ['https://shop.importo.eu/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"username": "info@auto-trade.com", "password": "auto123"},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on.
        if "authentication failed" in response.body:
            print 'eeeeeeeeeeeeeee'
            self.logger.error("Login failed")
            return
        
        # code to extract all links from given link.
        # extractor = LinkExtractor(allow_domains='shop.importo.eu')
        # links = extractor.extract_links(response)
        # print "Total links : ",len(links)

        # total_pages = response.xpath("//div[@class='pages']")
        # print total_pages
        
        # for link in links:
        #     print link.url
            # yield scrapy.Request(url=link.url, callback=self.getProductDetail)

        print '#'*100