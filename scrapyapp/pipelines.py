# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import MySQLdb
import os, datetime
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapyapp import settings
from slugify import slugify
import requests

class ScrapyappPipeline(object):
    def process_item(self, item, spider):
        return item

# pipeline for mysql storage in local system.
class MySQLStorePipeline(object):
    host = "localhost"
    user = "root"
    password = 'welcome'
    database = "jobs_provider"
    def __init__(self):
        self.connection = MySQLdb.connect( self.host, self.user, 
                                           self.password, self.database, 
                                           use_unicode=True, charset="utf8")
        self.cursor = self.connection.cursor()
        
    def process_item(self, item, spider):
        try:
            query="""INSERT INTO home_itemstesting (name, item_url, title, sku_number, upc_number, price, discount, create_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            params=('xyz', item['url'], item['title'], item['sku'], item['upc'], item['price'], item['discount'], str(datetime.datetime.now()), str(datetime.datetime.now()))
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as ex:
            self.connection.rollback()
        finally:
            self.connection.close()
    
# pipeline for mysql storage in local system.
class StoreImagesPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)
        
    def item_completed(self, results, item, info):
        for result in [x for ok, x in results if ok]:
            path = result['path']
            slug = slugify(item['upc'])

            # settings = get_project_settings()
            # storage = settings.get('IMAGES_STORE')
            storage = settings.IMAGES_STORE

            target_path = os.path.join(storage, slug, os.path.basename(path))
            path = os.path.join(storage, path)

            # If path doesn't exist, it will be created
            if not os.path.exists(os.path.join(storage, slug)):
                os.makedirs(os.path.join(storage, slug))

            if not os.rename(path, target_path):
                raise DropItem("Could not move image to target folder")
        return item

class StoreVideosPipeline(ImagesPipeline):
    
    def get_media_requests(self, item, info):
        for video_url in item['video_urls']:
            yield scrapy.Request(video_url, meta={'item': item})

    def media_downloaded(self, response, request, info):
        (vpath, vname) = os.path.split(request.url)
        item = response.meta['item']
        video_url = item['video_urls']
        local_filename = video_url.split('/')[-1]
        # NOTE the stream=True parameter
        r = requests.get(video_url, stream=True)
        with open(settings.FILES_STORE + str(local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
            # close file session
            f.close()

        # video_url = 'https://vipsandhu.com/download/video/1/26601/Difference-Amrit-Maan-360p-(Mr-Jatt.Com).mp4'
        # cap = cv2.VideoCapture(video_url)

        # output_path = '/home/gc14/Documents/fiverr/scrapyapp/scrapyapp/download/files/xyz.mp4'

        # # Define the codec and create VideoWriter object
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # out = cv2.VideoWriter(output_path, fourcc, 20.0, (200,200))

        # while(cap.isOpened()):
        #     ret, frame = cap.read()
        #     if ret:
        #         # write the flipped frame
        #         out.write(frame)

        #         cv2.imshow('frame',frame)
        #         if cv2.waitKey(1) & 0xFF == ord('q'):
        #             break
        #     else:
        #         break
            
        # cap.release()
        # out.release()
        # cv2.destroyAllWindows()

    # def item_completed(self, results, item, info):
    #     for result in [x for ok, x in results if ok]:
    #         path = result['path']
    #         slug = slugify(item['unique_key'])

    #         # settings = get_project_settings()
    #         # storage = settings.get('IMAGES_STORE')
    #         storage = settings.IMAGES_STORE

    #         target_path = os.path.join(storage, slug, os.path.basename(path))
    #         path = os.path.join(storage, path)

    #         # If path doesn't exist, it will be created
    #         if not os.path.exists(os.path.join(storage, slug)):
    #             os.makedirs(os.path.join(storage, slug))

    #         if not os.rename(path, target_path):
    #             raise DropItem("Could not move image to target folder")
    #     return item