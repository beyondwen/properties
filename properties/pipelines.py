# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json


class PropertiesPipeline(object):

    def __int__(self):
        self.file = codecs.open('basic.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print(item)
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()
