# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
import random

class DownloadvideosScrapySpider(scrapy.Spider):
    name = 'downloadvideos_scrapy'
    # allowed_domains = ['djjohal.com']
    start_urls = ['https://vipsandhu.com/Punjabi-Top-Videos-2018.html']

    def parse(self, response):
        # code to extract all links from given link.
        extractor = LinkExtractor(allow_domains='vipsandhu.com')
        links = extractor.extract_links(response)
        print "links : ",len(links)
        for link in links:
            yield scrapy.Request(url=link.url, callback=self.getProductDetail)
            break

    def getProductDetail(self, response):
        # code to extract download link.
        download_link_container = response.css(".download-links")
        if len(download_link_container):
            download_link = download_link_container[0].xpath(".//p")[2].xpath(".//a/@href").extract_first()
            if 'http' not in download_link:
                download_link = "https://vipsandhu.com" + str(download_link)
            yield {
                "unique_key": random.randint(100,201),
                "video_urls": [download_link]
            }
            # yield scrapy.Request(url=download_link, callback=self.downloadVideo)