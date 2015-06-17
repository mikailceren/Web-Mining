# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import log, Request
import scrapy
#comments:
#scrapy crawl SelectBook -o data.json
#scrapy crawl SelectBook
from Book.items import BookItem
from scrapy import log, Request
class SelectBookSpider(BaseSpider):
    name = "SelectBook"
    allowed_domains = ["kitapyurdu.com"]
    """start_urls = (
        'http://www.kitapyurdu.com/kitap/od--cd-ilaveli/261783.html&path=128/',
		'http://www.kitapyurdu.com/kitap/kurk-mantolu-madonna/12064.html&path=128',
		'http://www.kitapyurdu.com/kitap/fi/346913.html',
		'http://www.kitapyurdu.com/kitap/ask-pembe-kapak/125971.html&path=128',
		
    )"""
    start_urls = (
	    ['http://www.kitapyurdu.com/kitap/\w*/%s.html' % page for page in xrange(1000, 2001)]
	)

    def parse(self, response):		
		    items = []
		    item = BookItem()		    
		    item['url'] = response.url
		    item['title'] = response.xpath('//div[@class = "padding"]//h1/text()')[0].extract().encode("utf-8")
		    item['author'] = response.xpath('//span[@itemprop = "name"]/text()')[0].extract().encode("utf-8")
		    item['yayinevi'] = response.xpath('//span[@itemprop = "name"]/text()')[1].extract().encode("utf-8")
		    item['summary'] = response.xpath('//span[@itemprop = "description"]/text()')[0].extract().encode("utf-8")
		    item['language'] = response.xpath('//table[@class = "attribute"]//tr//td//span/text()')[1].extract().encode("utf-8")
		    item['date'] = response.xpath('//table[@class = "attribute"]//tr//td[@itemprop = "datePublished"]/text()')[0].extract()
		    item['genre'] = response.xpath('//div[@class = "grid_6 omega alpha section"]//a/text()')[2].extract().encode("utf-8")
		    item['image_urls'] = response.xpath('//div[@class = "image"]//a//img[@itemprop = "image"]/@src').extract()
		    item['price'] = response.xpath('//div[@class = "price-sales column-box mg-b-20"]//span[@class = "value"]/text()')[0].extract()
		    items.append(item)
		    return items
