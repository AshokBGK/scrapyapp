from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import xlsxwriter
import re, os, sys, time
options = Options()
options.add_argument('--headless')
 
class DimensionsHelper():

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options)

    # mothod to get items on webpage.
    def getItems(self):
        site_items = 0
        temp_site_items = 0
        total_items = []
        links = []
        try:
            # open url using webdriver.
            self.driver.get(self.url)
            try:
                # get total items on webpage.
                site_items = self.driver.find_element_by_xpath("//div[@data-bt='result_count_publication_plus']")
                site_items = str(site_items.text).replace(",", "").strip()
                site_items = int(site_items)
            except:
                pass

            if site_items > 0:
                while True:
                    try:
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(2)
                        articles = self.driver.find_elements_by_xpath("//article")
                        temp_site_items = len(articles)
                        if temp_site_items >= 988:
                            break
                    except:
                        pass

            # parse webpage into html.
            soup = BeautifulSoup(self.driver.page_source, "html.parser")
            # finding container element which have item list.
            container = soup.find("div", {"class": "infinite-scroll"})
            items = container.find_all("article")
            print("items : ",len(items))
            if len(items) > 0:
                count = 0
                for item in items:
                    count += 1
                    # print("item count : ",count)
                    try:
                        # finding product url.
                        item_url = item.find("a") 
                        if item_url:
                            item_url = "https://app.dimensions.ai" + str(item_url["href"]).strip()
                            links.append(item_url)
                    except:
                        pass
            else:
                print("Initial page have no item.")

        except:
            pass

        if len(links) > 0:
            print("Total links are : ",len(links))
            # Iteration over each link one by one.
            link_count = 0
            for link in links:
                # print("Item link : "+str(link))
                link_count += 1
                print("count : "+str(link_count))
                print('link : ',link)
                try:
                    # Call getItemDetail method to get item detaiil.
                    data = self.getItemDetail(link)
                    if len(data) > 0:
                        total_items.append(data)
                except:
                    pass
        
        # close webdriver session.
        self.driver.close()
        return total_items

    # method to get item detail.
    def getItemDetail(self, link):
        fields = {}
        try: 
            # open new HTTP session - this will keep alive our connection
            session = requests.Session()
            # create new session for product webpage.
            product_page = session.get(link)
            # create product_soup tree from product page
            product_soup = BeautifulSoup(product_page.text, 'html.parser')
            title = product_soup.find("h1", {"data-bt": "details-title"}).text
            # print("title : ",title)

            outlet = 'N/A'
            year = 'N/A'
            try:
                subTitle = product_soup.find("div", {"class": "details_title__subtitle details_title__subtitle--secondary"})
                try:
                    outlet = subTitle.find('a').text
                    try:
                        subTitle = str(subTitle.contents[2]).strip()[2:].strip()
                        subTitle = subTitle.split(",")
                        year = subTitle[-1]
                    except:
                        pass
                except:
                    pass
                
            except:
                pass
            # print("outlet : ",outlet)
            # print("year : ",year)
            
            try:
                doi = product_soup.find("a", {"data-bt": "doi_linkout"})['href']
            except:
                doi = 'N/A'
            # print("doi : ",doi)

            try:
                authors = product_soup.find("div", {"class": "details__involved"})
                authors = str(authors.text).strip()
            except:
                authors = 'N/A'
            # print("authors : ", authors)

            try:
                abstract = product_soup.find("div", {"class": "abstract"})
                abstract = str(abstract.text).strip()[:-5].strip()
            except:
                abstract = "N/A"
            # print("abstract : ",abstract)

            try:
                research = product_soup.find('span', text=re.compile(r'Research Categories'))
                if research:
                    research = research.find_parent('div').find_next_sibling()
                    research = research.find('ul').text
            except:
                research = 'N/A'
            # print("research : ", research)

            try:
                citiations = product_soup.find("div", {"class": "__dimensions_Badge_Image"})
            except:
                citiations = 'N/A'

            try:
                ratio = product_soup.find("div", {"class": "__dimensions_Badge_stat_group __dimensions_Badge_stat_group_cr"}).text
            except:
                ratio = 'N/A'
            
            fields['ItemURL'] = link
            fields['Title'] = title
            fields['Outlet'] = outlet
            fields['Year'] = year
            fields['DOI'] = doi
            fields['Authors'] = authors
            fields['Abstract'] = abstract
            fields['Research'] = research
            fields['Ratio'] = ratio
        except:
            pass

        session.close()
        return fields
    
    # method to write data to excel sheet.
    def writeExcelFile(self, items):
        try:
            print('Going to write data to excel file')
            # Create a workbook.
            workbook = xlsxwriter.Workbook('./dimensions.xlsx')
            # Create a worksheet.
            worksheet = workbook.add_worksheet('results')
            # Add a bold format to use to highlight cells.
            bold = workbook.add_format({'bold': 1})
            # Adjust the column width.
            worksheet.set_column(0, 1, 20)
            worksheet.set_column(4, 6, 20)
            # Excel file contains 10 columns.
            # Write some data headers.
            worksheet.write('A1', 'Item URL', bold)
            worksheet.write('B1', 'Title', bold)
            worksheet.write('C1', 'Outlet', bold)
            worksheet.write('D1', 'Year', bold)
            worksheet.write('E1', 'DOI', bold)
            worksheet.write('F1', 'Author', bold)
            worksheet.write('G1', 'Abstract', bold)
            worksheet.write('H1', 'Research', bold)
            worksheet.write('I1', 'Ratio', bold)
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
                    if 'Outlet' in key:
                        worksheet.write(row, col + 2,    value)
                    if 'Year' in key:
                        worksheet.write(row, col + 3, value)
                    if 'DOI' in key:
                        worksheet.write(row, col + 4, value)
                    if 'Authors' in key:
                        worksheet.write(row, col + 5, value)
                    if 'Abstract' in key:
                        worksheet.write(row, col + 6, value)
                    if 'Research' in key:
                        worksheet.write(row, col + 7, value)
                    if 'Ratio' in key:
                        worksheet.write(row, col + 8, value)
                row += 1
            workbook.close()
            print('Excelsheet written successfully.')
        except:
            print('Error occured while writing file.')
            print(sys.exc_info())
            pass

    def start(self):
        items = self.getItems()
        print("Total items are : ",len(items))
        if len(items) > 0:
            self.writeExcelFile(items)
        else:
            print('No item found.')


if __name__ == "__main__":

    items_url = 'https://app.dimensions.ai/discover/publication?search_text=Autism&search_type=kws&search_field=full_search&or_facet_year=2018&or_facet_publication_type_literal=article' 

    # objD is an instance for DimensionsHelper.
    objD = DimensionsHelper(items_url)
    objD.start()