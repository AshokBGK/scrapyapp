from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests, uuid, urllib
from bs4 import BeautifulSoup
from PIL import ImageFile, Image
import xlsxwriter
import re, os, sys
import base64, ast, json
options = Options()
options.add_argument('--headless')
 
class CostaballenaProperty():

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.PhantomJS(executable_path='.\\utility\\phantomjs.exe')

    # mothod to get products on webpage.
    def getProducts(self):
        # print("Initilization of products")
        list_products = []
        links = []
        try:
            # open url using webdriver.
            self.driver.get(self.url)
            # parse webpage into html.
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            # finding container element which have product list.
            container = soup.find("table", {"id": "_ctl4__ctl2__ctl0__ctl0_5578660_5578660_lsp_shortGrid"})
            products = container.find("tbody").find_all("tr")
            print("products : ",len(products))
            if len(products) > 0:
                count = 0
                for product in products:
                    count += 1
                    # print("product count : ",count)
                    try:
                        # finding product url.
                        product_url = product.find("a", {"class": "ViewListingLink"}) 
                        if product_url:
                            try:
                                new_constructions = str(product_url.find_next_sibling().text).replace("\n", "").strip()
                            except:
                                new_constructions = ''
                            product_url = str(product_url["href"]).replace("..", "").strip()
                            links.append({
                                "product_url": product_url,
                                "construction": new_constructions
                            })
                    except:
                        pass
            else:
                print("Initial page have no products.")

            # isProducts = True
            # page_count = 1
            # while isProducts:
            #     page_count += 1
            #     try:
            #         # finding next page url.
            #         next_page = self.driver.find_element_by_xpath("//a[contains(text(), 'Next >>')]")
            #         if next_page:
            #             page_break = next_page.get_attribute('disabled')
            #             if page_break:
            #                 break
            #             next_page.click()
            #             items = self.getNewPageProducts(self.driver.page_source)
            #             if len(items) > 0:
            #                 links.extend(items)
            #             else:
            #                 isProducts = False
            #                 break       
            #         else:
            #             isProducts = False
            #             break
            #     except:
            #         isProducts = False
            #         break

        except:
            pass

        if len(links) > 0:
            print("Total links are : ",len(links))
            # Iteration over each link one by one.
            link_count = 0
            for link in links:
                # print("Product link : "+str(link))
                link_count += 1
                print("link_count : "+str(link_count))
                try:
                    # Call getProductDetail method to get product detaiil.
                    data = self.getProductDetail(link)
                    if len(data) > 0:
                        list_products.append(data)
                except:
                    pass
                break
        
        # close webdriver session.
        self.driver.close()
        return list_products

    def getNewPageProducts(self, page_source):
        product_urls = []
        try:
            # parse web page into html tree.
            soup = BeautifulSoup(page_source, "html.parser")
            # finding container element which contains products.
            container = soup.find("table", {"id": "_ctl4__ctl2__ctl0__ctl0_5578660_5578660_lsp_shortGrid"})
            products = container.find("tbody").find_all("tr")
            if len(products) > 0:
                count = 0
                for product in products:
                    count += 1
                    # print("product count : ",count)
                    try:
                        # finding product url.
                        product_url = product.find("a", {"class": "ViewListingLink"})
                        if product_url:
                            try:
                                new_constructions = str(product_url.find_next_sibling().text).replace("\n", "").strip()
                            except:
                                new_constructions = ''
                            product_url = str(product_url["href"]).replace("..", "").strip()
                            product_urls.append({
                                "product_url": product_url,
                                "construction": new_constructions
                            })
                    except:
                        pass
        except:
            pass
        return product_urls

    # method to get product detail.
    def getProductDetail(self, link):
        # open new HTTP session - this will keep alive our connection
        session = requests.Session() 
        fields = {}
        print("item url : ",link['product_url'])
        try: 
            # create new session for product webpage.
            product_page = session.get(link['product_url'])
            # create product_soup tree from product page
            product_soup = BeautifulSoup(product_page.text, 'html.parser')
            title = product_soup.find("title").text

            try:
                city = product_soup.find("span", {"class": "locality"}).text
            except:
                city = ''

            try:
                locality = product_soup.find("span", {"itemprop": "addressLocality"}).text
            except:
                locality = ''

            try:
                region = product_soup.find("span", {"itemprop": "addressRegion"}).text
            except:
                region = ''
            
            try:
                country = product_soup.find("span", {"itemprop": "addressCountry"}).text
            except:
                country = ''

            try:
                postalCode = product_soup.find("span", {"itemprop": "postalCode"}).text
            except:
                postalCode = ''

            try:
                status = product_soup.find("span", {"class": "sold"}).text
            except:
                try:
                    status = ''
                    statusTemp = product_soup.find("div", {"class": "price"}).find_next_sibling().text
                    if 'sale' in statusTemp or 'sold' in statusTemp:
                        status = statusTemp
                except: 
                    status = ''
             
            address = city + ' (' + locality + ', ' + region + ', ' + country + ')' 
            address = address.replace("(,", '(')

            priceDetail = None
            try:
                priceDetail = product_soup.find("div", {"class": "price"})
                price = str(priceDetail.text).strip()
                if price:
                    # price = re.search("\d+", priceDetail).group()
                    price = ''.join(x for x in price if x.isdigit())
            except:
                price = ''
            
            agent_name = ''
            try:
                price_highlights_detail = priceDetail.find_next_sibling()
                price_highlights = str(price_highlights_detail.text).strip()
                if 'For Sale by' in price_highlights:
                    agent_name = price_highlights.split('For Sale by')[1].strip()
            except:
                price_highlights = ''

            latitude = ''
            longitude = ''
            # This is for getting latitude and longitude.
            try:
                scripts = product_soup.find_all('script')
                script = str(scripts[8].text).strip()
                script_data = script.split("groups")[1][4:-4].strip()
                script_data = json.loads(json.dumps(script_data))
                script_data = ast.literal_eval(script_data)
                latitude = script_data['points'][0]['y']
                longitude = script_data['points'][0]['x']
            except:
                pass
            
            fields['ItemURL'] = link['product_url']
            fields['Title'] = title
            fields['City'] = city
            fields['Address'] = address
            fields['zipCode'] = postalCode
            fields['Price'] = price
            fields['priceHighlights'] = price_highlights
            fields['Status'] = status
            fields['Neighborhood'] = city
            fields['newConstructions'] = link['construction']
            fields['latitude'] = latitude
            fields['longitude'] = longitude
            fields['agent_name'] = agent_name
            
            # This is for getting product listing data.
            listing_data = self.getProductListingData(product_soup)
            fields.update(listing_data)

            # This is for getting product sections data.
            sections_data = self.getProductSectionData(product_soup)
            fields.update(sections_data)

            try:
                brokeredBy = product_soup.find("div", {"class": "handshake-cnt"})
                if brokeredBy:
                    brokeredBy = brokeredBy.find("span").text
                    fields['brokeredBy'] = brokeredBy
            except:
                pass

            p2number = ''
            p2number_detail = product_soup.find("div", attrs={"class": "p2no"}).text
            if p2number_detail:
                p2number = str(p2number_detail).replace('P2#', '').strip()
            fields['P2#'] = p2number

            # This is for getting product images info.
            item_images = self.getProductImages(product_soup, p2number)
            fields['item_images'] = item_images
        except:
            pass

        session.close()
        return fields
    
    # method to get product listing data.
    def getProductListingData(self, productSoup):
        listing_data = {}
        try:
            categoryCountainer = productSoup.find("div", {"class": "listing-details-data"})
            categories = categoryCountainer.find_all("li")
            # print("total categories are : ",len(categories))
            try:
                general_highlights = categoryCountainer.find("span", {"class": "listing-details-general-highlight"}).text
            except:
                general_highlights = ''
            listing_data['generalHighlights'] = general_highlights

            if len(categories) > 0:
                for category in categories:
                    try:
                        cat_type = category.find(text=True)
                        cat_value = cat_type.next_sibling.text
                        cat_type = str(cat_type).replace(":", "").strip().lower()
                        cat_value = str(cat_value).strip()
                        if cat_type == "type":
                            listing_data['Type'] = cat_value
                        if cat_type == "style":
                            listing_data['Style'] = cat_value
                        if cat_type == 'development level':
                            listing_data['developmentLevel'] = cat_value
                        if cat_type == "size":
                            listing_data['Size'] = cat_value
                        if cat_type == 'suite':
                            listing_data['Suite'] = cat_value
                        if cat_type == "lot size":
                            listing_data['lotSize'] = cat_value
                        if cat_type == 'mls #':
                            listing_data['MLS'] = cat_value
                        if cat_type == "lot type":
                            listing_data['lotType'] = cat_value
                        if cat_type == 'garage':
                            listing_data['Garage'] = cat_value
                        if cat_value == 'garage type':
                            listing_data['garageType'] = cat_value
                        if cat_type == "taxes":
                            listing_data['Taxes'] = cat_value
                        if cat_type == "condo fees":
                            listing_data['condoFees'] = cat_value
                        if cat_type == "bedrooms":
                            listing_data['Bedrooms'] = cat_value
                        if cat_type == "bathrooms":
                            listing_data['Bathrooms'] = cat_value
                        if cat_type == 'half bathrooms':
                            listing_data['halfBathrooms'] = cat_value
                        if cat_type == "year built":
                            listing_data['yearBuilt'] = cat_value
                    except:
                        pass
        except:
            pass
        return listing_data

    # method to get product sections data.
    def getProductSectionData(self, productSoup):
        results = {}
        try:
            # This is for extracting descriptiion for product.
            try:
                description = productSoup.find("h3", text=re.compile(r"Description"))
                if description is not None:
                    description = description.find_next_sibling().text
                    results['Description'] = str(description).replace("\r\n", "").strip()
            except:
                description = ''

            # This is for extracting heighlights
            try:
                highlights = productSoup.find("h3", text=re.compile(r"Highlights"))
                if highlights is not None:
                    highlights = highlights.find_next_sibling()
                    results['Highlights'] = highlights.text
            except:
                pass

            # This is for extracting features for product.
            try:
                featuresContainer = productSoup.find("h3", text=re.compile(r'Features'))
                if featuresContainer is not None:
                    featuresContainer = featuresContainer.find_next_sibling()
                    features = featuresContainer.find_all("h4")
                    fe_names = ''
                    for feature in features:
                        try:
                            fname = str(feature.text).lower()
                            fe_names += str(fname) + ","
                            list_de = ''
                            try:
                                list_fe = feature.find_next_sibling()
                                list_sub_features = list_fe.find_all("li")
                                for li in list_sub_features:
                                    li = str(li.text) + ","
                                    list_de += li
                                fvalue = list_de
                            except:
                                fvalue = feature.find_next_sibling().text
                            fvalue = fvalue[:-1]
                            if 'interior features' in fname:
                                results['interiorFeatures'] = fvalue
                            if 'exterior finish' in fname:
                                results['exteriorFinish'] = fvalue
                            if 'roof' in fname:
                                results['Roof'] = fvalue
                            if 'view' in fname:
                                results['View'] = fvalue
                            if 'appliances' in fname:
                                results['Appliances'] = fvalue
                            if 'sewer/water systems' in fname:
                                results['sewerWaterSystems'] = fvalue
                            if 'lot features' in fname:
                                results['lotFeatures'] = fvalue
                            if 'extra features' in fname:
                                results['extraFeatures'] = fvalue
                            if 'cooling' in fname:
                                results['Cooling'] = fvalue
                            if 'heating' in fname:
                                results['Heating'] = fvalue
                            if 'buying options' in fname:
                                results['buyingOptions'] = fvalue
                        except:
                            pass

                    results['Features'] = fe_names
            except:
                pass
             
        except:
            pass
         
        return results

    def getLargeImages(self, images):
        images_data = []
        try:
            try:
                im = ImageFile.Parser()
                while True:
                    data = im.read()
                    break
            except:
                pass
            # set the dimentions for image.
            j = base64.b64encode(bytes(str(35), 'ascii'))
            k = int(base64.b64decode(j))
            t = len(images)
            pr = 50
            if t >= k:
                pr = 38
            p = base64.b64encode(bytes(str(pr), 'ascii'))
            q = base64.b64encode(bytes(str(100), 'ascii'))
            d = (int(base64.b64decode(p)) / int(base64.b64decode(q)) * len(images))
            r = d % 2
            d = int(d)
            if r > 0:
                d += 1
            images_data = images[:d]
        except:
            pass
        return images_data

    # method to get product images.
    def getProductImages(self, itemSoup, item_number):
        item_images = ''
        try:
            imagesContainer = itemSoup.find("div", {"class": "thumbs"})
            if imagesContainer:
                images = imagesContainer.find_all('img')
                images = self.getLargeImages(images)
                print('Going to save images.')
                image_count = 0
                for image in images:
                    image_count += 1
                    image_count = "{0:03}".format(image_count)
                    image_url = image['data-fullsrc']
                    # This is used to save images in local system.
                    item_image = self.writeImage(image_url, item_number, image_count)
                    if len(item_image) > 0:
                        item_image = str(item_image) + '|'
                        item_images += item_image
                    image_count = int(image_count)
                
                if len(item_images) > 0:
                    item_images = item_images[:-1]
                print('images saved successfully.')
        except:
            pass
        return item_images
    
    # method to write image in local system.
    def writeImage(self, img_url, item_number, image_count):
        filename_new = ''
        try:
            resource = urllib.request.urlopen(img_url)
            size = resource.headers.get("content-length")
            if size: 
                size = int(size)
                p = ImageFile.Parser()
                while True:
                    data = resource.read()
                    if not data:
                        break
                    p.feed(data)
                    if p.image:
                        # return size, p.image.size
                        # dimentions = list(p.image.size)
                         
                        filename, file_extension = os.path.splitext(img_url)
                        filename_new = str(item_number) + '-' + str(image_count) + str(file_extension)
                        images_dir = './images/' + str(item_number)
                        if not os.path.exists(images_dir):
                            os.makedirs(images_dir)
                            
                        image_path = images_dir + "/" + filename_new
                        # output = open(file_path, "wb")
                        # output.write(resource.read())
                        # output.close()
                        urllib.request.urlretrieve(img_url, image_path)
                    break
            resource.close()
        except:
            pass
        return filename_new

    def writeExcelFile(self, items):
        try:
            print('Going to write data to excel file')
            # Create a workbook.
            workbook = xlsxwriter.Workbook('./costaballenaproperty.xlsx')
            # Create a worksheet.
            worksheet = workbook.add_worksheet('results')
            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': 1})
            # Adjust the column width.
            worksheet.set_column(0, 39, 15)
            # worksheet.set_column(7, 12, 15)
            # Excel file contains 40 columns.
            # Write some data headers.
            worksheet.write('A1', 'Item URL', bold)
            worksheet.write('B1', 'Title', bold)
            worksheet.write('C1', 'Neighborhood', bold)
            worksheet.write('D1', 'Suite Number', bold)
            worksheet.write('E1', 'Address', bold)
            worksheet.write('F1', 'City', bold)
            worksheet.write('G1', 'Postal/Zip Code', bold)
            worksheet.write('H1', 'Status', bold)
            worksheet.write('I1', 'Price Highlight', bold)
            worksheet.write('J1', 'General Highlight', bold)
            worksheet.write('K1', 'New Consruction', bold)
            worksheet.write('L1', 'Style', bold)
            worksheet.write('M1', 'Garage', bold)
            worksheet.write('N1', 'Garage Type', bold)
            worksheet.write('O1', 'Type', bold)
            worksheet.write('P1', 'Bedrooms', bold)
            worksheet.write('Q1', 'Bathrooms', bold)
            worksheet.write('R1', 'Half Bathrooms', bold)
            worksheet.write('S1', 'Size', bold)
            worksheet.write('T1', 'Year Built', bold)
            worksheet.write('U1', 'Development Level', bold)
            worksheet.write('V1', 'MLS #', bold)
            worksheet.write('W1', 'Description', bold)
            worksheet.write('X1', 'Price', bold)
            worksheet.write('Y1', 'Features', bold)
            worksheet.write('Z1', 'Interior Features', bold)
            worksheet.write('AA1', 'Cooling', bold)
            worksheet.write('AB1', 'Exterior Finish', bold)
            worksheet.write('AC1', 'Roof', bold)
            worksheet.write('AD1', 'Appliances', bold)
            worksheet.write('AE1', 'Lot Features', bold)
            worksheet.write('AF1', 'View', bold)
            worksheet.write('AG1', 'Extra Features', bold)
            worksheet.write('AH1', 'Sewer/Water Systems', bold)
            worksheet.write('AI1', 'Heating', bold)
            worksheet.write('AJ1', 'Buying options', bold)
            worksheet.write('AK1', 'P2#', bold)
            worksheet.write('AL1', 'Taxes', bold)
            worksheet.write('AM1', 'Condo Fee', bold)
            worksheet.write('AN1', 'Lot Type', bold)
            worksheet.write('AO1', 'Lot Size', bold)
            worksheet.write('AP1', 'Brokered and Advertised by', bold)
            worksheet.write('AQ1', 'Latitude', bold)
            worksheet.write('AR1', 'Longitude', bold)
            worksheet.write('AS1', 'Agent', bold)
            worksheet.write('AT1', 'photoFile', bold)

            # Start from the first cell. Rows and columns are zero indexed.
            row = 1
            col = 0
            # Iterate over the data and write it out row by row.
            for item in items:
                for key, value in item.items():
                    if 'ItemURL' in key:
                        worksheet.write(row, col,    value)
                    if 'Title' in key:
                        worksheet.write(row, col + 1,    value)
                    if 'Neighborhood' in key:
                        worksheet.write(row, col + 2,    value)
                    if 'Suite Number' in key:
                        worksheet.write(row, col + 3, value)
                    if 'Address' in key:
                        worksheet.write(row, col + 4, value)
                    if 'City' in key:
                        worksheet.write(row, col + 5, value)
                    if 'zipCode' in key:
                        worksheet.write(row, col + 6, value)
                    if 'Status' in key:
                        worksheet.write(row, col + 7, value)
                    if 'priceHighlights' in key:
                        worksheet.write(row, col + 8, value)
                    if 'generalHighlights' in key:
                        worksheet.write(row, col + 9, value)
                    if 'newConstructions' in key:
                        worksheet.write(row, col + 10, value)
                    if 'Style' in key:
                        worksheet.write(row, col + 11, value)
                    if  key == 'Garage':
                        worksheet.write(row, col + 12, value)
                    if 'garageType' in key:
                        worksheet.write(row, col + 13, value)
                    if key == 'Type':
                        worksheet.write(row, col + 14, value)
                    if 'Bedrooms' in key:
                        worksheet.write(row, col + 15, value)
                    if key == 'Bathrooms':
                        worksheet.write(row, col + 16, value)
                    if 'halfBathrooms' in key:
                        worksheet.write(row, col + 17, value)
                    if key == 'Size':
                        worksheet.write(row, col + 18, value)
                    if 'yearBuilt' in key:
                        worksheet.write(row, col + 19, value)
                    if 'developmentLevel' in key:
                        worksheet.write(row, col + 20, value)
                    if 'MLS' in key:
                        worksheet.write(row, col + 21, value)
                    if 'Description' in key:
                        worksheet.write(row, col + 22, value)
                    if 'Price' in key:
                        worksheet.write(row, col + 23, value)
                    if key == 'Features':
                        worksheet.write(row, col + 24, value)
                    if 'interiorFeatures' in key:
                        worksheet.write(row, col + 25, value)
                    if 'Cooling' in key:
                        worksheet.write(row, col + 26, value)
                    if 'exteriorFinish' in key:
                        worksheet.write(row, col + 27, value)
                    if key == 'Roof':
                        worksheet.write(row, col + 28, value)
                    if key == "Appliances":
                        worksheet.write(row, col + 29, value)
                    if 'lotFeatures' in key:
                        worksheet.write(row, col + 30, value)
                    if key == 'View':
                        worksheet.write(row, col + 31, value)
                    if 'extraFeatures' in key:
                        worksheet.write(row, col + 32, value)
                    if 'sewerWaterSystems' in key:
                        worksheet.write(row, col + 33, value)
                    if 'Heating' in key:
                        worksheet.write(row, col + 34, value)
                    if 'buyingOptions' in key:
                        worksheet.write(row, col + 35, value)
                    if 'P2#' in key:
                        worksheet.write(row, col + 36, value.replace("P2#", '').strip())
                    if 'Taxes' in key:
                        worksheet.write(row, col + 37, value)
                    if 'condoFees' in key:
                        worksheet.write(row, col + 38, value)
                    if 'lotType' in key:
                        worksheet.write(row, col + 39, value)
                    if 'lotSize' in key:
                        worksheet.write(row, col + 40, value)
                    if 'brokeredBy' in key:
                        worksheet.write(row, col + 41, value)
                    if 'latitude' in key:
                        worksheet.write(row, col + 42, value)
                    if 'longitude' in key:
                        worksheet.write(row, col + 43, value)
                    if 'agent_name' in key:
                        worksheet.write(row, col + 44, value)
                    if 'item_images' in key:
                        worksheet.write(row, col + 45, value)
                row += 1
            workbook.close()
            print('Excelsheet written successfully.')
        except:
            print('Error occured while writing file.')
            pass

    def start(self):
        products = self.getProducts()
        if len(products) > 0:
            self.writeExcelFile(products)
        else:
            print('No products found.')
        

if __name__ == "__main__":

    products_url = 'http://www.costaballenaproperty.com/Neighborhood/page_2681716.html' 
    # objCP is an instance for CostaballenaProperty.
    objCP = CostaballenaProperty(products_url)
    objCP.start()
    
    