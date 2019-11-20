# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class PropertiesItem(scrapy.Item):
    title = scrapy.Field()
    totalPrice = scrapy.Field()
    houseInfo = scrapy.Field()
    followInfo = scrapy.Field()
