# -*- coding: utf-8 -*-
import scrapy

class PrimitivesbykathySpider(scrapy.Spider):
    name = 'primitivesbykathy'
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

        item_url = "https://wholesale.primitivesbykathy.com/shop"
        yield scrapy.Request(url=item_url, callback=self.getProducts)

    # method to get products.
    def getProducts(self, response):
        # code to get total pages.
        total_pages = response.xpath("//a[@class='last']/text()").extract_first()
        if total_pages:
            total_pages = int(total_pages)
        
        # update range for urls
        for d in range(1, total_pages):
            product_url = "https://wholesale.primitivesbykathy.com/shop?p="+str(d)
            yield scrapy.Request(url=product_url, callback=self.getProductLinks)

    # method to parse products link.
    def getProductLinks(self, response):
        # Going to get total products on a webpage.
        products = response.xpath("//li[@class='item last']")
        if len(products):
            for product in products:
                product_url = product.xpath(".//div[@class='product-info']/h2/a/@href").extract_first()
                yield scrapy.Request(url=product_url, callback=self.getProductDetail)

    # method to get product detail.
    def getProductDetail(self, response):       
        # this is for get product title.
        title = response.xpath("//div[@class='product-shop']/div/span/text()").extract_first()
        # this is for get product UPC.
        product_upc = response.xpath("//th[contains(text(), 'UPC')]/following-sibling::td/text()").extract_first()
        if product_upc:
            product_upc = str(product_upc).strip()
        # this is for get product SKU.
        product_sku = response.xpath("//div[@class='product-sku']/span[2]/text()").extract_first()
        if product_sku:
            product_sku = product_sku.lower().strip().replace('wholesale', '').replace('-', '').strip()
        # this is for get product price.
        price = response.xpath("//div[@class='price-box']/span/span/text()").extract_first()
        # this is for get product discount.
        discount = response.xpath("//div[@class='case-discount-price']/p/span/text()").extract_first()
        if discount:
            discount = str(discount).strip()

        yield {
            "URL": response.url,
            "title": title,
            "upc": product_upc,
            "sku": product_sku,
            "price": price,
            "discount": discount,
        }