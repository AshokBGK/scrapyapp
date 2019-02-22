from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
print "Going to start spider from external script."
os.chdir(r'/home/gc14/Documents/fiverr/scrapyapp')
process = CrawlerProcess(get_project_settings())
process.crawl('downloadImages_scrapy', domain='darice.com')
process.start()
print '#####################################'