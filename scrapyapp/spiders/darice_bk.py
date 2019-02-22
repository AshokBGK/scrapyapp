# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class DariceSpider(scrapy.Spider):
    name = 'darice_bk'
    # allowed_domains = ['www.darice.com']
    start_urls = ['https://www.darice.com/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"EmailAddress": "peter@theredheadllc.com", "AccountPassword": "TempPass123"},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on.
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # code to extract all links from given link.
        # extractor = LinkExtractor(allow_domains='darice.com')
        # links = extractor.extract_links(response)
        # for link in links:
        #     yield scrapy.Request(url=link.url, callback=self.getProductDetail)

        rules = (
            Rule(LinkExtractor(), callback='parse_item', follow=True),
        )

    # method to get product detail.
    def getProductDetail(self, response):
        products = response.css('.product')
        if len(products):
            for product in products:
                # this is for get product url.
                product_url = product.xpath(".//div[@class='productDetails']/div/a/@href").extract_first()
                if 'http' not in product_url:
                    product_url = 'https://www.darice.com' + str(product_url)
                # this is for get product title.
                title = product.xpath(".//meta[@itemprop='name']/@content").extract_first()
                # this is for get product UPC.
                product_upc = product.xpath(".//meta[@itemprop='gtin12']/@content").extract_first()
                # this is for get product SKU.
                product_sku = product.xpath(".//meta[@itemprop='productID']/@content").extract_first()
                # this is for get product price.
                price = product.xpath(".//div[@class='productPrice']/text()").extract_first()
                if price:
                    price = str(price).lower().strip().replace('your price :', '').strip()
                
                yield {
                    "URL": product_url,
                    "title": title,
                    'upc': product_upc,
                    'sku': product_sku,
                    'price': price,
                }
        