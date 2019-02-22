# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    # allowed_domains = ['www.darice.com']
    start_urls = ['https://www.darice.com/']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={"EmailAddress": "peter@theredheadllc.com", "AccountPassword": "TempPass123"},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        product_urls = [
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-beads-acrylic-tri-beads',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-beads-acrylic-alpha',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-beads-acrylic-pony',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-beads-strands-pearls',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-findings-earrings-fish-hook',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-findings-earrings-hoops',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-findings-clasps-lobster',
            # 'https://www.darice.com/store/browse/catalog/wholesale-jewelry-findings-clasps-magnetic',
            # 'https://www.darice.com/store/browse/catalog/wholesale-basics-miniature-ornaments',
            # 'https://www.darice.com/store/browse/catalog/wholesale-basics-miniature-flocked',
            # 'https://www.darice.com/store/browse/catalog/wholesale-basics-miniature-timeless',
            # 'https://www.darice.com/store/browse/catalog/wholesale-basics-paper-mache',
            # 'https://www.darice.com/store/browse/catalog/wholesale-kids-art',
            # 'https://www.darice.com/store/browse/catalog/wholesale-kids-basics',
            # 'https://www.darice.com/store/browse/catalog/wholesale-kids-project-plan-it',
            # 'https://www.darice.com/store/browse/catalog/wholesale-bridal-candles-lighting',
            # 'https://www.darice.com/store/browse/catalog/wholesale-bridal-floral',
            # 'https://www.darice.com/store/browse/catalog/wholesale-bridal-attire',
            'https://www.darice.com/store/browse/catalog/wholesale-bridal-favors',
            # 'https://www.darice.com/store/browse/catalog/wholesale-wood-chalkboards-and-corkboards',
        ]
        for product_url in product_urls:
            yield scrapy.Request(url=product_url, callback=self.getProductDetail)

    def getProductDetail(self, response):
        products = response.css('.product')
        print "products : ",len(products)
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
                print "product_url : ",product_url
                print "title : ",title
                print "product_upc : ",product_upc
                print "product_sku : ",product_sku
                print "price : ",price
                print "#"*100
                