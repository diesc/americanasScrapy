# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmericanasscrapyItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    breadcrumb = scrapy.Field()
    img = scrapy.Field()
    seller = scrapy.Field()
    price = scrapy.Field()