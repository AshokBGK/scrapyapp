from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from captcha_solver import CaptchaSolver
import requests
from bs4 import BeautifulSoup
# from xlrd import open_workbook
import base64
import re, os, sys, time
options = Options()
options.add_argument('--headless')
 
class DropshipingHelper():

    def __init__(self):
        self.url = ''
        # self.driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options)
        self.driver = webdriver.Chrome(executable_path='/home/gc14/Downloads/chromedriver')
    
    def createOrder(self):
        print "Going to create new order."
        item_url = 'https://www.aliexpress.com/store/product/comfortable-Summer-T-Shirts-Fortnite-Battle-Royale-Legend-Gaming-Pattern-Tops-Baby-Girls-Boys-T-shirt/3208096_32874541326.html?spm=2114.search0104.3.1.3f2a54c9uMrya8&ws_ab_test=searchweb0_0,searchweb201602_1_10152_10065_10151_5011811_10344_10068_10342_10343_10340_10059_10341_10696_100031_10084_10083_10103_10618_10307_10624_10623_10622_10621_10620_5723611_5011711,searchweb201603_13,ppcSwitch_5&algo_expid=4e531641-26b7-404a-9967-d2305559edc9-0&algo_pvid=4e531641-26b7-404a-9967-d2305559edc9&priceBeautifyAB=0'
        print 'item_url : ',item_url
        self.driver.get(item_url)
        time.sleep(2)

        # user authentication
        signIn_btn = self.driver.find_element_by_xpath("//a[@data-role='sign-link']")
        self.driver.execute_script('arguments[0].click();', signIn_btn)
        time.sleep(2)
        
        iframe = self.driver.find_element_by_xpath("//iframe[@id='alibaba-login-box']")
        self.driver.switch_to_frame(iframe)
        auth_email = self.driver.find_element_by_xpath("//input[@name='loginId']")
        auth_email.send_keys("gcrew.surinder@gmail.com")

        auth_pass = self.driver.find_element_by_xpath("//input[@name='password']")
        auth_pass.send_keys("developertesting123")

        auth_submit = self.driver.find_element_by_xpath("//input[@name='submit-btn']")
        self.driver.execute_script('arguments[0].click();', auth_submit)
        self.driver.switch_to_default_content()
        time.sleep(5)

        # validate_btn = self.driver.find_element_by_id("nc_1_n1z")
        # print "validate_btn : ",validate_btn
        # webdriver.ActionChains(self.driver).click_and_hold(validate_btn).move_by_offset(260, 0).click().perform()
        # time.sleep(3)
        # captcha_image = self.driver.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']")
        # if captcha_image:
        #     captcha_image = captcha_image.find_element_by_xpath(".//img").get_attribute("src")
        #     captcha_image = captcha_image.split('base64,')[1].strip()
        #     f = open('test.jpg', 'wb+')
        #     f.write(base64.decodestring(captcha_image))
        #     f.close()
        #     print 'file written successfully.'

        #     # img_text = captcha_image.decode('base64')
        #     # print "img_text : "
        #     # print img_text

        #     solver = CaptchaSolver('browser')
        #     raw_data = open('test.png', 'rb').read()
        #     print(solver.solve_captcha(raw_data))

        # this is used to select item color.
        sku_element = self.driver.find_element_by_id("sku-1-200001438")
        self.driver.execute_script('arguments[0].click();', sku_element)
        # this is used to select item size.
        item_size = self.driver.find_element_by_id("sku-2-200004198")
        self.driver.execute_script('arguments[0].click();', item_size)
        # this is used to select buy button
        buy_btn = self.driver.find_element_by_id("j-buy-now-btn")
        self.driver.execute_script('arguments[0].click();', buy_btn)
        # buy_btn.click()
        time.sleep(2)
        # # print self.driver.page_source

        # print "#"*100
        # # going to create order.
        # email = self.driver.find_element_by_xpath("//input[@name='email']")
        # print "email : ",email
        # email.send_keys("gcrew.surinder@gmail.com")

        # contact_name = self.driver.find_element_by_name("contactPerson")
        # print "contact_name : ",contact_name  
        # contact_name.send_keys("SurinderB")

        # country = self.driver.find_element_by_name("country")
        # # country.send_keys("United States")
        # selected_country = Select(country)

        # # select by visible text
        # selected_country.select_by_visible_text('United States')

        # address = self.driver.find_element_by_name("address")
        # address.send_keys("New York")

        # state = self.driver.find_element_by_xpath("//select[@data-spm-anchor-id='a2g0s.13010108.99999999.i2.2541321eDn6KjD']")
        
        # selected_state = Select(state)

        # # select by visible text
        # selected_state.select_by_visible_text('California')

        # city = self.driver.find_element_by_name("city")
        # city.send_keys("New York")

        # # zip = self.driver.find_element_by_name("zip")
        # # zip.send_keys("15202")

        # # mobile = self.driver.find_element_by_name("mobileNo")
        # # mobile.send_keys("98456234")

        # save_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Save and ship to this address')]")
        # self.driver.execute_script('arguments[0].click();', save_btn)
        print('Order created successfully.')

    # mothod to get items on webpage.
    def getInputFromExcel(self):
        items = []
        rows = []
        try:
            # this is used to open excel file.
            wb = open_workbook('./products.xlsx')
            # now to get first sheet from excel file.
            sheet = wb.sheets()[0]
            # this is used to get rows and column count.
            number_of_rows = sheet.nrows
            number_of_columns = sheet.ncols
            # print number_of_rows
            # print number_of_columns
            for row in range(1, number_of_rows):
                values = []
                for col in range(number_of_columns):
                    value  = (sheet.cell(row,col).value)
                    try:
                        value = str(int(value))
                    except ValueError:
                        pass
                    finally:
                        values.append(value)
                items.append(values)
        except:
            pass
        return items

    def start(self):
        # items = self.getInputFromExcel()
        # print("Total items are : ",len(items))
        # if len(items) > 0:
        #     self.createOrder(items)
        # else:
        #     print('No item found.')
        self.createOrder()


if __name__ == "__main__":

    # objD is an instance for DropshipingHelper.
    objD = DropshipingHelper()
    objD.start()