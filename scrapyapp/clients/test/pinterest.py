# -*- coding: utf-8 -*-
# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import sys

class PinterestHelper():
    
    def __init__(self):
        self.domain = "https://tr.pinterest.com/"

    def getResults(self):
        item_url = self.domain + 'source/bestlouboutinshop.com/'
        print "item_url : ",item_url
        res = requests.get(item_url)
        soup = BeautifulSoup(res.text, u'html.parser')
        # print soup
        products = soup.findAll('div', attrs={'data-test-id':'pinWrapper'})
        print "Total : ",len(products)

    def start(self):
        self.getResults()

if __name__ == '__main__':
    # objPH is an instance for PinterestHelper.
    objPH = PinterestHelper()
    objPH.start()