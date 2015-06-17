# -*- coding: utf-8 -*-

# Scrapy settings for Babil project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'Babil'

SPIDER_MODULES = ['Babil.spiders']
NEWSPIDER_MODULE = 'Babil.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Babil (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 1
HTTPCACHE_ENABLED = True

DOWNLOAD_DELAY = 2.0

ITEM_PIPELINES = {
    'Babil.pipelines.BabilPipeline': 500,
	'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}
IMAGES_STORE = 'C:\Users\TOSHIBA\Desktop\Babil\Babil\IMAGES_STORE'
