# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import sys, time

class ImportoHelper():
    
    def __init__(self):
        # self.driver = webdriver.PhantomJS('/home/gc14/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver = webdriver.Chrome("/home/gc14/Documents/fiverr/scrapyapp/scrapyapp/utility/chromedriver")
        self.job_url = 'https://shop.importo.eu/'

    def getItems(self):
        results = []
        try:
            self.driver.get(self.job_url)
            self.driver.set_window_size(1124, 850)
            # code to authenticate user on this website.
            self.driver.find_element_by_name("username").send_keys("info@auto-trade.com")
            self.driver.find_element_by_name("password").send_keys("auto123")
            self.driver.find_element_by_name("send").submit()
            time.sleep(3)

            print 'yyyyyy'
            # total_items = self.driver.find_element_by_xpath("//div[@class='summary']/strong").text
            total_items = 1033
            print "total_items : ",total_items
            print type(total_items)
            items = 0
            while items <= total_items:
                try:
                    page_products = self.getProducts(self.driver.current_url)
                    items += len(page_products)
                    results.extend(page_products)
                    next_btn = ''
                    # next_btn.click()
                    time.sleep(2)
                except:
                    break
        except:
            print sys.exc_info()

        print '#################'
        # close webdriver session.
        # self.driver.close()
        return results

    def getProducts(self, items_url):
        products = []
        try:
            res = requests.get(items_url)
            soup = BeautifulSoup(res.text, u'html.parser')
            container = soup.find("table", attrs={"class": "table table-hover products table-striped"})
            products = container.findAll('tr')
        except:
            pass
        return products

    def getProductDetail(self, items):
        try:
            for item in items:
                print item
                break
        except:
            print sys.exc_info()

    def start(self):
        print 'wwwwww'
        items = self.getItems()
        if len(items):
            self.getProductDetail(items)

if __name__ == '__main__':
    
    #objIH is an instance for ImportoHelper.
    objIH = ImportoHelper()
    objIH.start()

    