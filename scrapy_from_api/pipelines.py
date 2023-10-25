# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import logging


class ScrapyFromApiPipeline:
    collection_name = 'vietnam_provinces'
    connection = '' # Input your connection
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.connection)
        self.db = self.client['learning']
    def process_item(self, item, spider):
        collection_name =self.db[self.collection_name]
        collection_name.insert_one(item)
        return item

    def close_spider(self, item, spider):
        self.client.close()