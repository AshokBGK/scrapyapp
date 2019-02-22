# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb
import datetime, time
import sys

class VivanunciosHelper():

    def __init__(self, url):
        self.item_url = url
        self.driver = webdriver.PhantomJS('./phantomjs')

    def getAddressInfo(self, postcode):
        postcode_results = []
        try:
            # Going to open url using webdriver.
            self.driver.get(self.item_url)
            time.sleep(2)
            
            verder_btn = self.driver.find_element_by_xpath("//input[@name='akkoord']")
            verder_btn.click()
            
            time.sleep(2)
            # soup = BeautifulSoup(self.driver.page_source, u'html.parser')
            # time.sleep(3)
            address_input = self.driver.find_element_by_id('zoeklocatie')
            address_input.send_keys(postcode)
            search_btn = self.driver.find_element_by_id('zoeklocatieSubmit')
            search_btn.click()
            time.sleep(2)
            result_cont = self.driver.find_element_by_id('adLijst')
            results = result_cont.find_elements_by_xpath(".//a")
            print str(len(results)) + " results found."
            if len(results):
                for result in results:
                    result.click()
                    time.sleep(5)
                    adres = self.driver.find_element_by_id('polygoon_adres').find_element_by_xpath(".//td").text
                    postcode = self.driver.find_element_by_id('polygoon_postcode').find_element_by_xpath(".//td").text
                    woonplaats = self.driver.find_element_by_id('polygoon_woonplaats').find_element_by_xpath(".//td").text
                    dict_data = {
                        'item': result.text,
                        'address': adres,
                        'postcode': postcode,
                        'woonplaats': woonplaats
                    }
                    postcode_results.append(dict_data)
        except:
            pass

        # close webdriver session.
        self.driver.close()
        return postcode_results

    def savePostcodeAddress(self, data):
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd="test123", db="my_jobs")
            cursor = conn.cursor()
            for d in data:
                query = "INSERT INTO scraper_postcodedetail (item, address, postcode, place, created_at, updated_at)"
                query += " VALUES "
                query += "('" + d['item'] + "', '" + d['address'] + "', '" + d['postcode'] + "', '" + d['woonplaats'] + "', '" + str(datetime.datetime.now()) + "', '"  + str(datetime.datetime.now()) + "')"
                query += " ON DUPLICATE KEY UPDATE item = '" + d['item'] + "', address = '" + d['address'] + "', postcode = '" + d['postcode'] + "', place = '" + d['woonplaats'] + "', updated_at = '" + str(datetime.datetime.now()) + "';"
                cursor.execute(query)
                conn.commit()
        except:
            pass
        finally:
            cursor.close()
            conn.close()

    def startProcess(self):
        # put all postal code here.
        postcode_lst = ['9712CA', '9712AA', '9712AE', '9712AM']
        count = 0
        while True:
            try:
                postcode = postcode_lst[count]
                data = self.getAddressInfo(postcode)
                print "data : ",len(data)
                # if len(data):
                #     self.savePostcodeAddress(data)

                count += 1
                if count >= len(postcode_lst):
                    break
            except:
                pass

    def getProducts(self):
        list_items = []
        count = 0
        try:
            while True:
                print "item_url : ",self.item_url
                self.driver.get(self.item_url)
                time.sleep(2)
                items = self.driver.find_elements_by_xpath("//a[@class='href-link tile-title-text']")
                print "Total : ",len(items)
                list_items.extend(items)
                count += len(items)
                next_btn = self.driver.find_element_by_xpath("//a[@class='arrows icon-right-arrow']")
                if next_btn:
                    next_btn.click()
                    time.sleep(2)

                if count > 20:
                    break
        except:
            print sys.exc_info()
            pass
        return list_items

    def start(self):
        print "Going to start process."
        list_items = self.getProducts()      

if __name__ == "__main__":

    item_url = 'https://www.vivanuncios.com.mx/s-venta-inmuebles/v1c1097p1'

    # objVH is an instance for VivanunciosHelper
    objVH = VivanunciosHelper(item_url)
    objVH.start()