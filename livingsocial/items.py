# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LivingSocialDeal(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    location = scrapy.Field()
    original_price = scrapy.Field()
    price = scrapy.Field()
    end_date = scrapy.Field()
