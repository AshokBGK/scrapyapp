# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        products_links = [
            "https://www.amazon.com/s/ref=nb_sb_ss_i_2_7?url=search-alias%3Daps&field-keywords=tshirts+for+mens&sprefix=tshirts%2Caps%2C397&crid=3QZCB51RP72UV",
        ]

        for link in products_links:
            yield scrapy.Request(url=link, callback=self.getProductsLinks)

    def getProductsLinks(self, response):
        products = response.xpath("//div[@id='atfResults']/ul/li")
        print "Total : ",len(products)
        if len(products):
            for product in products:
                product_url = product.xpath(".//div/div/div/a/@href").extract_first()
                if "http://" not in product_url:
                    product_url = "https://www.amazon.com" + str(product_url)
                yield scrapy.Request(url=product_url, callback=self.getProductDetail)
                break
        else:
            print "No product found."

    def getProductDetail(self, response):
        print 'ppppppp'
        print response.url
        title = response.xpath("//span[@id='productTitle']/text()").extract_first()
        if title:
            title = str(title).strip()
        price = response.xpath("//span[@id='priceblock_ourprice']/text()").extract_first()
        asin = response.xpath("//span[@id='fitRecommendationsSection']/@data-asin").extract_first()
        stars = response.xpath("//span[@id='acrPopover']/@title").extract_first()
        if stars:
            stars = stars.strip().split()[0].strip()
            # stars = int(stars)
        reviews = response.xpath("//span[@id='acrCustomerReviewText']/text()").extract_first()
        published_date = response.xpath("//span[contains(text(), 'Date first listed on Amazon:')]/following-sibling::*/text()").extract_first()
        print "title : ",title
        print "price : ",price
        print "stars : ",stars
        print "asin : ",asin
        print "published_date : ",published_date
        print "reviews : ",reviews
        print '#'*100
        
        
