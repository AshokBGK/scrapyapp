# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

class TractorpartsasapSpider(scrapy.Spider):
    name = 'tractorpartsasap'
    allowed_domains = ['tractorpartsasap.com']
    start_urls = [
        'https://www.tractorpartsasap.com'
        # 'https://www.tractorpartsasap.com/parts-categories.html',
        # 'https://www.tractorpartsasap.com/universal-parts.html',
        # 'https://www.tractorpartsasap.com/tractor-accessories.html',
        # 'https://www.tractorpartsasap.com/farm-shop-supplies.html',
        # 'https://www.tractorpartsasap.com/farm-shop-supplies/gifts-toys-accessories.html'
    ]

    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(allow=('parts-categories', )), callback='parse'),
    # )

    def parse(self, response):
        # import re
        # code to extract all links from given link.
        extractor = LinkExtractor(
            allow=('parts-categories/', 
            'universal-parts/', 
            'tractor-accessories/', 
            'farm-shop-supplies/'
        ), allow_domains='tractorpartsasap.com')
        links = extractor.extract_links(response)
        print "links : ",len(links)
        for link in links:
            # print link.url
            yield scrapy.Request(url=link.url, callback=self.getProductLink)
            # yield scrapy.Request(url=link.url, callback=self.getProductDetail)
            # break

        # item_url = 'https://www.tractorpartsasap.com/parts-categories/combine-parts/case-ih-combine-parts/1660/engine-parts.html'
        # yield scrapy.Request(url=item_url, callback=self.getProductLink)

    def getProductLink(self, response):
        # print 'welcome to get link method.'
        # print response.url
        sub_links = response.css('.subcategory_link')
        # print "Total sub_links : ",len(sub_links)
        if len(sub_links):
            for sub_link in sub_links:
                sub_link = sub_link.xpath(".//@href").extract_first()
                # print "sub_link : ",sub_link
                cart_btn = response.xpath("//button[@title='Add to Cart']")
                if cart_btn:
                    yield scrapy.Request(url=sub_link, callback=self.getProductDetail)
                else:
                    yield scrapy.Request(url=sub_link, callback=self.secondLevelItems)

            # This is to get next web page link
            # next_page_link = response.xpath("//a[@title='Next']/@href").extract_first()
            # if next_page_link:
            #     yield scrapy.Request(url=next_page_link, callback=self.getProductLink)

    def secondLevelItems(self, response):
        # print 'welcome to second level.'
        sub_links = response.css('.subcategory_link')
        # print "Total sub_links : ",len(sub_links)
        if len(sub_links):
            for sub_link in sub_links:
                sub_link = sub_link.xpath(".//@href").extract_first()
                # print "sub_link222222 : ",sub_link
                yield scrapy.Request(url=sub_link, callback=self.getProductsFromLink)

    def getProductsFromLink(self, response):
        # print "welcome to total products"
        # print response.url
        products = response.css(".item.product.product-item")
        # print "Products : ",len(products)
        if len(products):
            for product in products:
                product_url = product.xpath(".//div/a/@href").extract_first()
                yield scrapy.Request(url=product_url, callback=self.getProductDetail)

    def getProductDetail(self, response):
        # this is for get product title.
        title = response.xpath("//span[@itemprop='name']/text()").extract_first()

        # this is for get product SKU.
        item_sku = response.xpath("//div[@itemprop='sku']/text()").extract_first()

        # this is for get product price.
        price = response.xpath("//span[@class='price']/text()").extract_first()

        # this is for get product description.
        description_data = response.xpath("//div[@class='product attribute description']/div/ul/li")
        
        description = ''
        if len(description_data):
            for d in description_data:
                try:
                    n = d.xpath(".//text()").extract_first()
                    n = str(n).strip() + '\n'
                    description += n
                except:
                    pass

        image = response.xpath("//ul[@id='ovimage-thumbs']/li/a/img/@src").extract_first()
        # print "images : ",len(images)
        # image = 'Image'
        # if len(images):
        #     count = 0
        #     for i in images:
        #         count += 1
        #         img = i.xpath(".//a/img/@src").extract_first()
        #         image += 1

        yield {
            'URL': response.url,
            'title': title,
            'price': price,
            'sku': item_sku,
            'image': image,
            'description': description
        }

        # print "title : ",title
        # print "item_sku : ",item_sku
        # print "price : ",price
        # print "img : ",image
        print '#'*100
