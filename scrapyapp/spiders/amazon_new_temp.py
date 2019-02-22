# -*- coding: utf-8 -*-
import scrapy


class AmazonNewTempSpider(scrapy.Spider):
    name = 'amazon_new_temp'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.in/GeekCases-Primo-1-8M-Braided-Gunmetal/dp/B07GCPRW85/ref=zg_bs_10894234031_36?_encoding=UTF8&psc=1&refRID=B0T2E9N8CQYG7B175E02']

    def parse(self, response):

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
        
        publish_date = response.xpath("//tr[@class='date-first-available']/td")[-1]
        if publish_date:
            publish_date = publish_date.xpath(".//text()").extract_first()
        product_detail.update({"publish_date": publish_date})

        # warranty_status = response.xpath("//div[@id='wns']/text()").extract_first()
        # print("warranty_status : ",warranty_status)

        # technical_detail = response.xpath("//div[@class='column col1']")
        # additional_info = response.xpath("//div[@class='column col2']")

        # print technical_detail
        # print additional_info
        # print product_detail
        print "#"*100
