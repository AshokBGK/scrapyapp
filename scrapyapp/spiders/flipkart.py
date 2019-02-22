# -*- coding: utf-8 -*-
import scrapy


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/']

    def parse(self, response):
        links = [
            "https://www.flipkart.com/mens-clothing/tshirts/pr?sid=2oq,s9b,j9y&otracker=nmenu_sub_Men_0_T-Shirts",
        ]

        for link in links:
            yield scrapy.Request(url=link, callback=self.getProductsLinks)

    def getProductsLinks(self, response):
        products = response.xpath("//a[@class='Zhf2z-']/@href").extract()
        print "Total : ",len(products)
        if len(products):
            for product in products:
                if "http" not in product:
                    product = "https://www.flipkart.com" + str(product)
                product_url = product
                yield scrapy.Request(url=product_url, callback=self.getProductDetail)
                break
        else:
            print "No products found."

    def getProductDetail(self, response):
        print 'ppppppp'
        print response.url
        title = response.xpath("//span[@class='_35KyD6']/text()").extract_first()
        if title:
            title = str(title).strip()
        price = response.xpath("//div[@class='_1vC4OE _3qQ9m1']/text()").extract_first()
        asin = response.xpath("//span[@id='fitRecommendationsSection']/@data-asin").extract_first()
        stars = response.xpath("//div[@class='hGSR34 _2beYZw']/text()").extract_first()
        # if stars:
        #     stars = stars.strip().split()[0].strip()
            # stars = int(stars)
        import json
        json_data = response.xpath("//*[@id='jsonLD']/text()").extract_first()
        if json_data:
            json_data = str(json_data).strip()
        print 'dddddddddddddddddd : ',type(json_data)
        print json_data
        reviews = response.xpath("//div[@class='swINJg _3nrCtb']/text()").extract_first()
        published_date = response.xpath("//span[contains(text(), 'Date first listed on Amazon:')]/following-sibling::*/text()").extract_first()
        print "title : ",title
        print "price : ",price
        print "stars : ",stars
        print "asin : ",asin
        print "published_date : ",published_date
        print "reviews : ",reviews
        print '#'*100
        
