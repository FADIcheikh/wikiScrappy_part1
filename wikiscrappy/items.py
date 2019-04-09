# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WikiscrappyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    day = scrapy.Field()
    month = scrapy.Field()
    urlx = scrapy.Field()