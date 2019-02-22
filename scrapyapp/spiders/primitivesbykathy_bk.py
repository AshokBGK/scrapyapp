# -*- coding: utf-8 -*-
import scrapy

class PrimitivesbykathySpider(scrapy.Spider):
    name = 'primitivesbykathy_bk'
    # allowed_domains = ['https://wholesale.primitivesbykathy.com']
    start_urls = ['https://wholesale.primitivesbykathy.com/customer/account/login/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"login[username]": "peter@theredheadllc.com", "login[password]": "TempPass123"},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # update range for urls
        for d in range(1, 20):
            product_url = "https://wholesale.primitivesbykathy.com/shop?p="+str(d)
            yield scrapy.Request(url=product_url, callback=self.getProductDetail)

    # method to get product detail.
    def getProductDetail(self, response):
        products = response.xpath("//li[@class='item last']")
        if len(products):
            for product in products:
                # this is for get product url.
                product_url = product.xpath(".//div[@class='product-info']/h2/a/@href").extract_first()
                # this is for get product title.
                title = product.xpath(".//div[@class='product-info']/h2/a/text()").extract_first()
                # # this is for get product UPC.
                # product_upc = product.xpath(".//meta[@itemprop='gtin12']/@content").extract_first()
                # this is for get product SKU.
                product_sku = product.xpath(".//div[@class='product-sku']/span[2]/text()").extract_first()
                if product_sku:
                    product_sku = product_sku.lower().strip().replace('wholesale', '').replace('-', '').strip()
                # this is for get product price.
                price = product.xpath(".//div[@class='price-box']/span/span/text()").extract_first()
                data = {
                    'product_url': product_url,
                    'product_sku': product_sku,
                    'title': title,
                    'price': price
                }
                yield scrapy.Request(url=product_url, callback=self.getProductUPC, meta=data)
    
    def getProductUPC(self, response):
        # this is for get product UPC.
        product_upc = response.xpath("//th[contains(text(), 'UPC')]/following-sibling::td/text()").extract_first()
        if product_upc:
            product_upc = str(product_upc).strip()
        data = response.meta
        yield {
            "URL": data['product_url'],
            "title": data['title'],
            'upc': product_upc,
            'sku': data['product_sku'],
            'price': data['price'],
        }