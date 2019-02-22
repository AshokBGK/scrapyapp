import base64
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import argparse
# pytesseract.tesseract_cmd = r'C:/Python27/Lib/site-packages/tesseract'

# import requests, io
# import cv2
# print 'wwwwwww'
# print( cv2.__version__ )
# from tesseract import image_to_string
# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = 'C:\Python27\Lib\site-packages\pytesseract\pytesseract.exe'
image_data = 'data:image/jpg;base64,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'.split("base64,")[1].replace(" ", "+")
print 'aaaaaa'
# d = base64.b64encode(image_data)
e = base64.b64decode(image_data)
# print e
# print image_to_string(Image.open('test.png'))
fh = open("test.jpg", "wb")
fh.write(e)
fh.close()
print 'file written success.'
# response = requests.get("test.png")
# img = Image.open(io.BytesIO(response.content))
# img = Image.open('test.png')
# print( type(img) ) # <class 'PIL.JpegImagePlugin.JpegImageFile'>
# text = image_to_string(img)
# text = image_to_string(image='test.png')
# print( text )
# img = img.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(img)
# img = enhancer.enhance(2)
# img = img.convert('1')
# img.save('temp2.jpg')
# print img.text
# tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
# pytesseract.pytesseract.tesseract_cmd = 'C:/Python27/Lib/site-packages/pytesseract/pytesseract.exe'
# text = pytesseract.image_to_string(Image.open('test.png'), lang='chi_sim')

# text = pytesseract.image_to_string(Image.open('images2.png')) working
# argparser = argparse.ArgumentParser()
# argparser.add_argument('path', help = 'Captcha file path')
# args = argparser.parse_args()
# path = args.path

# img = cv2.imread("test.jpg", 0)
# ret, = cv2.threshold(img, 10, 255)
# ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
# print "Threshold selected : ", img
# image = Image.open('test.png')
# print image
# code = pytesseract.image_to_string(image)
# print code
img = Image.open('test.jpg')
print img
for x in range(img.width):
    for y in range(img.height):
        if img.getpixel((x, y)) < (100, 100, 100):
            img.putpixel((x, y), (256, 256, 256))
gray = img.convert('L')
two = gray.point(lambda x: 0 if 68 < x < 90 else 256)
min_res = two.filter(ImageFilter.MinFilter)
med_res = min_res.filter(ImageFilter.MedianFilter)
for _ in range(2):
    med_res = med_res.filter(ImageFilter.MedianFilter)
res = pytesseract.image_to_string(med_res, config='-psm 6')
# print two
print res
print "hhhhh"

# file = open("test.png", "rb")
# r = file.read()
# print 'rrrrr'
# print r
# file.close()
