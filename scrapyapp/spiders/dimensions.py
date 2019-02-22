# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import sys, time
import re, json
import ast

class DimensionsSpider(scrapy.Spider):
    name = 'dimensions'
    # allowed_domains = ['https://app.dimensions.ai']
    start_urls = ['https://app.dimensions.ai/discover/publication?search_text=Autism&search_type=kws&search_field=full_search&or_facet_year=2018&or_facet_publication_type_literal=article']

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='../utility/chromedriver')
        # self.driver = webdriver.PhantomJS(executable_path='.\\utility\\phantomjs.exe')
        # self.driver = webdriver.Chrome(executable_path='/home/gc14/Downloads/chromedriver')

    def parse(self, response):
        links = []
        site_items = 0
        temp_site_items = 0

        try:
            # get total items on webpage.
            items_text = response.xpath("//div[@data-bt='result_count_publication_plus']/text()").extract_first()
            site_items = str(items_text).replace(",", "").strip()
            site_items = int(site_items)
        except:
            pass

        items_url = "https://app.dimensions.ai/discover/publication.contents.more.html"
        self.driver.get(items_url)

        initial_articles = self.driver.find_elements_by_xpath("//article")
        print "Total items are : ",len(initial_articles)
        if len(initial_articles) > 0:
            for initial_article in initial_articles:
                try:
                    link = initial_article.find_element_by_xpath(".//a")
                    link = "https://app.dimensions.ai" + str(link.get_attribute("data-href"))
                    links.append(link)
                except:
                    pass
        
        temp_site_items += len(initial_articles)
        if site_items > 0:
            while True:
                try:
                    load_more_btn = self.driver.find_element_by_xpath("//a[@data-js='infinite-scroll-load']")
                    if load_more_btn:
                        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        # time.sleep(2)
                        load_more_btn.click()
                        time.sleep(1)
                        articles = self.driver.find_elements_by_xpath("//article")
                        # print "new items : ",len(articles) 
                        if len(articles) > 0:
                            for article in articles:
                                try:
                                    link = article.find_element_by_xpath(".//a")
                                    link = "https://app.dimensions.ai" + str(link.get_attribute("data-href"))
                                    links.append(link)
                                except:
                                    pass
                        temp_site_items += len(articles)
                        if temp_site_items >= 1000:
                            break
                    else:
                        break
                except:
                    break
            else:
                print("No items found.")
            # print "temp_site_items : ",len(temp_site_items)

        if len(links) > 0:
            for link in links:
                yield scrapy.Request(url=link, callback=self.getItemDetail)

    # method to get item detail.
    def getItemDetail(self, response):
        fields = {}
        try:
            title = response.xpath("//h1[@data-bt='details-title']/text()").extract_first()
        except:
            title = 'N/A'
        # print "title : ",title

            outlet = 'N/A'
        year = 'N/A'
        try:
            subTitle = response.xpath("//div[@class='details_title__subtitle details_title__subtitle--secondary']")
            try:
                outlet = subTitle.xpath('.//a/text()').extract_first()
                try:
                    subTitle = subTitle.xpath("child::text()")
                    subTitle = subTitle[1].extract()
                    subTitle = subTitle.split(",")
                    year = subTitle[-1].strip()
                except:
                    pass
            except:
                pass
        except:
            pass
        # print "outlet : ",outlet
        # print "year : ",year
            
        try:
            doi = response.xpath("//a[@data-bt='doi_linkout']/@href").extract_first()
        except:
            doi = 'N/A'
        # print "doi : ",doi
            
        try:
            author_data = response.xpath("//div[@data-bt='details-main']/script/text()").extract_first()
            author_data = str(author_data).replace('var doc =', '').replace('null', 'None').strip()
            author_data = author_data.split('involved:')[1][:-1].strip()
            authors = list(ast.literal_eval(author_data))[0]
            auth = ''
            if len(authors) > 0:
                for author in authors:
                    try:
                        author = str(author['first_name']) + ' ' + str(author['last_name']) + ' - ' + str(author['affiliations'][0]['name']) + "\n"
                        auth += author
                    except:
                        pass
                if len(auth) > 0:
                    authors = auth
                else:
                    authors = "N/A"
            else:
                authors = 'N/A'
        except:
            authors = 'N/A'
        # print "authors : ", authors

        try:
            abstract_data = response.css(".abridged_text__layout::text").extract_first()
            abstract = abstract_data.encode('utf-8').strip()
        except:
            abstract = "N/A"
        # print "abstract : ",abstract

        research = "N/A"
        try:
            temp_research = response.xpath("//div[@data-js='research-categories']/@data-entities").extract_first()
            temp_research = temp_research.encode('utf-8')
            temp_research = ast.literal_eval(temp_research)
            temp_research = temp_research['for']['data']
            if len(temp_research) > 0:
                resrch = '' 
                for r in temp_research:
                    r = str(r['details']['name']) + '\n'
                    resrch += r
                if len(resrch) > 0:
                    research = resrch
                else:
                    research = "N/A"
            else:
                research = "N/A"
        except:
            research = 'N/A'
        # print "research : ", research

        try:
            citiations_data = response.xpath("//div[@data-js='figshare']/following-sibling::script")
            citiations_data = citiations_data[1].xpath(".//text()").extract_first()
            citiations_data = str(citiations_data).replace('config.related_documents.push(', '').strip()[:-2].strip()
            citiations = citiations_data.replace("null", "None").replace('false', 'False')
            citiations = ast.literal_eval(citiations)
            citiations = citiations['count']
        except:
            citiations = 'N/A'
        # print "citiations : ",citiations

        try:
            ratio = response.xpath("//div[@class='__dimensions_Badge_stat_group __dimensions_Badge_stat_group_cr']/text()").extract_first().default('N/A')
        except:
            ratio = 'N/A'
        # print "ratio : ",ratio

        yield {
            'ItemURL' : response.url,
            'Title' : title,
            'Outlet' : outlet,
            'Year' :  year,
            'DOI': doi,
            'Authors': authors,
            'Abstract': abstract,
            'Research': research,
            'Ratio': ratio
        }
    