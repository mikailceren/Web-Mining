# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BookItem(Item):
	
	title = Field()
	author = Field()
	yayinevi = Field()
	summary = Field()
	language = Field()
	date = Field()
	genre =Field()
	price = Field()
	life = Field()
	image_urls = Field()
	images = Field()
	url = Field()


