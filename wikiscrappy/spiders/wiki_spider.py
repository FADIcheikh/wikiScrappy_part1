# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import WikiscrappyItem

class WikiSpiderSpider(scrapy.Spider):
    name = 'wiki_spider'
    start_urls = ['https://en.wikipedia.org/wiki/January_1']

    def parse(self, response):
        #instanciation Item
        items = WikiscrappyItem()
        #initialisation
        day_one = '/wiki/January_1'
        # recuperer toutes les dates contenues dans le tableau
        all_days = response.css('tbody tr td li a::attr(href)').extract()
        # ignorer le dernier element => list_of_non-standard_dates
        all_days.pop(-1)
        all_days.insert(0,day_one)

        for day in all_days:
            next_url ='https://en.wikipedia.org/'+str(day)
            # recuper day et month
            day = re.search('([A-Za-z]*)_([0-9]*)', day)
            month = day.group(1)
            day = day.group(2)

            #print ('month : ' + str(month) + ' day:'+ str(day))
            items ['day'] = day
            items ['month'] = month
            items ['urlx'] = next_url
            yield items
            #yield response.follow(next_url, callback=self.parse)