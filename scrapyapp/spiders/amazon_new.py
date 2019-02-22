# -*- coding: utf-8 -*-
import scrapy

class AmazonNewSpider(scrapy.Spider):
    name = 'amazon_new'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/gp/bestsellers/']

    def parse(self, response):
        links = response.xpath("//ul[@id='zg_browseRoot']/ul/li")
        print("links : ",len(links))
        if len(links):
            for link in [links[0]]:
                link = link.xpath("./a/@href").extract_first()
                yield scrapy.Request(url=link, callback=self.getPage)
        print("#"*200)
        
    def getPage(self, response):
        page_title = response.xpath("//div[@id='zg-right-col']/h1/span/text()").extract_first()
        print(page_title)
        page_links = response.xpath("//ul[@id='zg_browseRoot']/ul/ul/li")
        print(len(page_links))
        if len(page_links):
            for page_link in [page_links[0]]:
                page_link = page_link.xpath("./a/@href").extract_first()
                yield scrapy.Request(url=page_link, callback=self.getPageProducts)
                # break
        
        print("F"*50)

    def getPageProducts(self, response):
        print("Going to get product:")
        products = response.xpath("//ol[@id='zg-ordered-list']/li")
        print("products : ",len(products))
        if len(products):
            for product in [products[0]]:
                product_link = product.xpath(".//a[@class='a-link-normal']/@href").extract_first()
                if 'http' not in product_link:
                    product_link = "https://www.amazon.in" + product_link
                yield scrapy.Request(url=product_link, callback=self.getProductDetail)
        print("J"*100)

    def getProductDetail(self, response):
        print("Going to get product detail")
        product_detail = {
            'title': None,
            'ASIN': None,
            'author': None,
            'rating': 0,
            'reviews_count': 0,
            'price': 0,
            'publish_date': None,
            'description': None,
            'images': []
        }

        title = response.xpath("//div[@id='titleSection']/h1/span/text()").extract_first()
        if title:
            title = str(title).strip()
        product_detail.update({'title': title})

        asin = response.xpath("//input[@id='ASIN']/@value").extract_first()
        product_detail.update({"ASIN": asin})

        author = response.xpath("//a[@id='bylineInfo']/text()").extract_first()
        product_detail.update({'author': author})
        
        rating = response.xpath("//span[@id='acrPopover']/@title").extract_first()
        if rating:
            rating = str(rating).split()[0].strip()
        product_detail.update({'rating': rating})

        reviews_count = response.xpath("//span[@id='acrCustomerReviewText']/text()").extract_first()
        if reviews_count:
            reviews_count = str(reviews_count).split()[0].strip()
        product_detail.update({'reviews_count': reviews_count})

        price = response.xpath("//span[@id='priceblock_saleprice']/text()").extract_first()
        product_detail.update({"price": price})

        desc_lis = response.xpath("//div[@id='feature-bullets']/ul/li")
        product_des = ""
        if len(desc_lis):
            for li in desc_lis:
                li = li.xpath(".//text()").extract_first()
                if li:
                    li = str(li).strip() + "\n"
                    product_des += li
        product_detail.update({"description": product_des})

        images = response.xpath("//div[@id='altImages']/ul/li")
        product_images = []
        if len(images):
            for image in images:
                image = image.xpath(".//img/@src").extract_first()
                if image:
                    product_images.append(image)
        product_detail.update({"images": product_images})
        
        publish_date = response.xpath("//tr[@class='date-first-available']/td")
        if publish_date:
            publish_date = publish_date[-1].xpath(".//text()").extract_first()
        product_detail.update({"publish_date": publish_date})

        print("K"*100)