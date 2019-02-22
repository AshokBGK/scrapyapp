# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

item_url = ''
res = requests.get(item_url)
soup = BeautifulSoup(res.text, u'html.parser')
print soup