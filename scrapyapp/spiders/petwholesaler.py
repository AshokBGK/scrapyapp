# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import scrapy
from scrapy.crawler import CrawlerProcess
# from scrapyapp.items import PetwholesalerItems


class PetwholesalerSpider(scrapy.Spider):
    name = 'petwholesaler'
    # allowed_domains = ['https://www.petwholesaler.com']
    start_urls = ['https://www.petwholesaler.com/search.php?mode=search&page=1']

    def parse(self, response):
        print("Do you want to extract data.")
        print response.url
        # This is used to get list of products from single page.
        products = response.xpath("//div[@id='products-list']/div")
        print "products : ",len(products)
        for product in products:
            # This is to get product link that contains product detail.
            product_link = product.xpath("descendant::div")[2].xpath("./a/@href").extract_first()
            # This is to concate to response url.
            link = response.urljoin(product_link)
            # It generate a new request to extract data from new url.
            yield scrapy.Request(url=link, callback=self.getProductDetail)
            print product_link

        # # This is to get next web page link
        # next_page_link = response.css("a.right-arrow::attr(href)").extract_first()
        # if next_page_link:
        #     # print 'there are more page available : '
        #     next_page_url = "https://www.petwholesaler.com/" + str(next_page_link)
        #     # print next_page_url
        #     yield scrapy.Request(url=next_page_url, callback=self.parse)

        pass

    def getProductDetail(self, response):
        print "yyyyyyy"
        item = PetwholesalerItems()
        title = response.xpath('//title/text()').extract_first()
        product_props = response.xpath("//div[@class='product-properties']")
        upc_number = product_props.xpath("//div[contains(text(), 'UPC')]/following-sibling::div/text()").extract_first()
        sku_number = product_props.xpath("//span[@id='manufacturercode']/text()").extract_first()
        price = product_props.xpath("//span[@id='product_prices']/text()").extract_first()
        print(upc_number, sku_number, price, title)
        item['UPC'] = upc_number
        item['SKU'] = sku_number
        item['price'] = price
        item['title'] = title
        yield item
        print '*'*100
        pass

if __name__ == "__main__":

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(PetwholesalerSpider)
    process.start() # the script will block here until the crawling is finished
