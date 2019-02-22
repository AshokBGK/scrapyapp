print "welcome to test.py"
import base64
import cv2
from PIL import Image
import pytesseract
from subprocess import check_output
import sys
import argparse
import numpy as np
from matplotlib import pyplot as plt
import Tkinter


# image_base64 = 'data:image/jpg;base64,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'.split('base64,')[1].strip()

# f = open('test.tif', 'wb+')
# f.write(base64.decodestring(image_base64))
# f.close()
# print 'file written successfully.'

# img = cv2.imread("test.tif", 0)
# ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
# cv2.imwrite("./debug.png", thresh)
# print ret, thresh

# myText = image_to_string(Image.open("test.png"),config='-psm 10')
# myText = image_to_string(Image.open("test.tif"))
# print "wwwwwwww"
# print myText

# argparser = argparse.ArgumentParser()
# argparser.add_argument('path',help = 'Captcha file path')
# # args = argparser.parse_args()
# # path = args.path
# path = 'test.jpg'
# print('Resolving Captcha')
# k = check_output(['convert', path, '-resample', '600', path])
# captcha_text = pytesseract.image_to_string(Image.open(path))
# print captcha_text

# img = cv2.imread('test.png',0)
# img = cv2.medianBlur(img,5)
# ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#             cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#             cv2.THRESH_BINARY,11,2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#             'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [img, th1, th2, th3]
# for i in xrange(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
#     print plt.text(0.5, 0.5, 'matplotlib')
# plt.show()
# print 'qqqqqqqqqqq'

# gray = cv2.LoadImage('test.jpeg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
# img = cv2.imread('test.png',0)
# cv2.Threshold(img, img, 231, 255, cv2.CV_THRESH_BINARY)
# import tesseract
# import pytesseract
# import sys
# import argparse
# try:
#     import Image
# except ImportError:
#     from PIL import Image
# from subprocess import check_output
# argparser = argparse.ArgumentParser()
# argparser.add_argument('path',help = 'Captcha file path')
# args = argparser.parse_args()
# path = args.path
# print('Resolving Captcha')
# check_output(['convert', path, '-resample', '600', path])
# text = pytesseract.image_to_string(Image.open(path))
# print text

# from PIL import Image
# # import ImageEnhance
# img = Image.open('test.jpeg')
# img = img.convert("RGB")
# box = (8, 8, 58, 18)
# img = img.crop(box)
# pixdata = img.load()
# print pixdata
# letters = Image.open('letters.bmp')
# ledata = letters.load()
# print ledata

# from selenium import webdriver
# url = 'https://www.aliexpress.com/store/product/comfortable-Summer-T-Shirts-Fortnite-Battle-Royale-Legend-Gaming-Pattern-Tops-Baby-Girls-Boys-T-shirt/3208096_32874541326.html?spm=2114.search0104.3.1.21e877bb5QE4Uz&ws_ab_test=searchweb0_0,searchweb201602_1_10152_10065_10151_10344_10068_10342_10343_10340_10059_10341_10696_100031_10084_10083_5011611_10103_10618_10307_10624_10623_5011511_10622_10621_10620_5723611,searchweb201603_13,ppcSwitch_5&algo_expid=fc3aef80-7853-4ae2-9fbf-b302b42ec70c-0&algo_pvid=fc3aef80-7853-4ae2-9fbf-b302b42ec70c&priceBeautifyAB=0'
# # driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
# driver = webdriver.Chrome(executable_path='/home/gc14/Downloads/chromedriver')
# driver.get(url)
# select_color = driver.find_element_by_xpath("//a[@data-sku-id='1254']")
# select_color.click()
# size = driver.find_element_by_xpath("//a[@data-sku-id='200004196']")
# size.click()
# buy_btn = driver.find_element_by_xpath("//a[@id='j-buy-now-btn']")
# buy_btn.click()
# import time
# time.sleep(3)
# email = driver.find_element_by_xpath("//input[@name='email']")
# email.send_keys('surindersuri315@gmail.com')

# save_btn = driver.find_element_by_xpath("//a[@class='ui-button ui-button-primary ui-button-medium sa-confirm']")
# save_btn.click()
# signIn = driver.find_element_by_xpath("//a[@class='signIn']")
# signIn.click()
# time.sleep(2)
# login_email = driver.find_element_by_xpath("//input[@id='fm-login-id']")
# login_email.send_keys('surindersuri315@gmail.com')
# password = driver.find_element_by_id("fm-login-password")
# password.send_keys("developertesting123")
# sin_btn = driver.find_element_by_id("fm-login-submit")
# sin_btn.click()
# time.sleep(3)
# from captcha_solver import CaptchaSolver
# solver = CaptchaSolver('browser')
# raw_data = open('test.png', 'rb').read()
# print(solver.solve_captcha(raw_data))


for d in range(1, 10):
    print d
