# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import sys, time
import csv

class MobileDeHelper():
    
    def __init__(self):
        # self.driver = webdriver.PhantomJS('/home/gc14/Downloads/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        self.driver = webdriver.Chrome("/home/gc14/Documents/fiverr/scrapyapp/scrapyapp/utility/chromedriver")
        self.job_url = "https://home.mobile.de/AUTO-DISCOUNT-KOSTHEIM#ses"

    def getItems(self):
        results = []
        try:
            self.driver.get(self.job_url)
            self.driver.set_window_size(1124, 850)

            while True:
                try:
                    load_more_btn = self.driver.find_element_by_css_selector('.btn.btn-inverse.CTALevel4')
                    # print "load_more_btn : ",load_more_btn
                    if load_more_btn:
                        # load_more_btn.click()
                        self.driver.execute_script("arguments[0].click()", load_more_btn);
                        time.sleep(3)
                        more_results = self.driver.find_element_by_css_selector(".moreResults")
                        more_results_style = more_results.get_attribute("style")
                        if 'none' in more_results_style:
                            break
                except:
                    break
            
            soup = BeautifulSoup(self.driver.page_source, u'html.parser')
            container = soup.find("div", {"class": "ses"})
            items = container.find('ul').findAll('li')
            if len(items):
                for item in items:
                    item_data = self.getProductDetail(item)
                    if len(item_data):
                        results.append(item_data)
            else:
                print("No item found.")
            
        except:
            pass

        # close webdriver session.
        self.driver.close()
        return results
    
    # method to get product detail.
    def getProductDetail(self, item):
        item_detail = {}
        try:
            # code to extract item title.
            title = item.find('h3')
            if title:
                title = unicode(title.text).encode('utf-8').replace(';', '').strip()
            
            image = item.find('img')['src'].encode('utf-8')

            # code to extract item usage.
            usage_type = item.find("span", {"class": "usageType"})
            if usage_type:
                usage_type = unicode(usage_type.text).encode('utf-8')

            # code to extract item body type.
            body_type = item.find("span", {"class": "bodyType"})
            if body_type:
                body_type = unicode(body_type.text).encode('utf-8')
            
            # code to extract item first peg.
            first_reg = item.find("span", {"class": "firstReg"})
            if first_reg:
                first_reg = unicode(first_reg.text).encode('utf-8')

            # code to extract item speed.
            speed = item.find("span", {"class": "hidden-phone"})
            if speed:
                speed = unicode(speed.text).encode('utf-8')

            # code to extract item fuel type.
            fuel_type = item.find("span", {"class": "fuelType"})
            if fuel_type:
                fuel_type = unicode(fuel_type.text).encode('utf-8')
            
            # code to extract item engine type.
            engine = item.find("span", {"class": "fuelType hidden-phone"})
            if engine:
                engine = unicode(engine.text).encode('utf-8')
            
            # code to extract item price.
            price = item.find("div", {"class": "vehiclePrice"}).text
            currency_type = 'USD'
            if price:
                price = unicode(price).encode('utf-8')
                if '€' in price:
                    currency_type = 'EURO'
                price = price.strip().split('€')[0].strip()
                
            item_detail = {
                "title": title,
                "image": image,
                "usage_type": usage_type,
                "body_type": body_type,
                "first_reg": first_reg,
                "speed": speed,
                "fuel_type": fuel_type,
                "engine": engine,
                "price": price,
                "currency_type": currency_type
            }
        except:
            pass

        return item_detail
    
    # method to write csv file.
    def writeCSVFile(self, items):
        print "Going to write csv file."
        try:
            with open('sample_cars.csv', mode='w') as csv_file:
                fieldnames = ['title', 'image', 'price', 'currency_type', 'fuel_type', 'speed', 'engine', 'first_reg', 'body_type', 'usage_type']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                writer.writeheader()
                for item in items:
                    writer.writerow(
                        {
                            'title': item['title'],
                            'image': item['image'],
                            'price': item['price'], 
                            'currency_type': item['currency_type'],
                            'fuel_type': item['fuel_type'],
                            'speed': item['speed'],
                            'engine': item['engine'],
                            'first_reg': item['first_reg'],
                            'body_type': item['body_type'],
                            'usage_type': item['usage_type']
                        }
                    )
            csv_file.close()
        except:
            print(sys.exc_info())
            pass
        print('File written successfully.')

    def start(self):
        items = self.getItems()
        print("Total items : ",len(items))
        if len(items):
            self.writeCSVFile(items)

# main function call
if __name__ == '__main__':
    #objMH is an instance for MobileDeHelper.
    objMH = MobileDeHelper()
    objMH.start()

    