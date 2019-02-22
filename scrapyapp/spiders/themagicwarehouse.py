# -*- coding: utf-8 -*-
import scrapy


class ThemagicwarehouseSpider(scrapy.Spider):
    name = 'themagicwarehouse'
    allowed_domains = ['http://themagicwarehouse.com']
    start_urls = ['http://themagicwarehouse.com/tall/magic-tricks.html']

    def parse(self, response):
        # print response
        items = response.css('.itemname')
        print "Total items : ",len(items)
        if len(items):
            for item in items:
                # print item
                # print type(item)
                title = item.xpath(".//h3/text()").extract_first()
                if title:
                    title = str(title).strip()
                print "title : ",title

                image = item.xpath("../../preceding-sibling::div")[-1].xpath(".//img/@src").extract_first()
                print "image : ",image 
                
                price = item.xpath("../following-sibling::span").xpath("./text()").extract_first()
                if price:
                    price = unicode(price).strip().lower()
                    if 'now' in price:
                        price = price.split('now')[-1].strip()
                print "price : ",price

                description = item.xpath("../following-sibling::p").xpath("./text()").extract_first()
                if description:
                    description = unicode(description).strip()
                # print "description : "
                # print description
                
                if title:
                    yield {
                        "title": title,
                        "price": price,
                        "image": image,
                        "description": description
                    }
                    print "#"*100
                # break
        pass
