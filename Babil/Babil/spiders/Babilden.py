# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy

from Babil.items import BabilItem
from scrapy import log, Request


class BabildenSpider(BaseSpider):
    name = "Babilden"
    allowed_domains = ["babil.com"]

    start_urls = (
	    ['http://www.babil.com/urunler/%s/' % page for page in xrange(1300500, 1301000)]
	)

    def parse(self, response):
		    items = []
		    item = BabilItem()
		    item['url'] = response.url
		    item['title'] = response.xpath('//div//h2[@itemprop = "name"]/text()').extract()[0].strip()
		    item['author'] = response.xpath('//div//span[@class = "author"]/text()')[0].extract().replace(" ","").strip()
		    item['yayinevi'] = response.xpath('//div//span[@class = "othor"]/text()').extract()[0].strip()
		    item['summary'] = response.xpath('//div[@class = "detail-box"]/text()').extract()[1].strip()
		    item['language'] = response.xpath('//div[@class = "left"]//div[2]//ul//li[4]//div//div/text()').extract()[2].strip()
		    item['date'] = response.xpath('//div[@class = "left"]//div[2]//ul//li[1]//div//div/text()').extract()[2].strip()
		    item['genre'] = response.xpath('//div//span[@class = "othor"]/text()').extract()[1].strip()
		    item['image_urls'] = response.xpath('//div[@class = "product-image turkce-kitap type-PaperBoard"]//img[@class = "big_image_one big_image"]/@src').extract()
		    item['price'] = response.xpath('//div//span[@class = "price price-sale"]/text()').extract()[0].replace(" ","").strip()
		    items.append(item)
		    return items
        
