from scrapy.http import Request
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
import MySQLdb
import MySQLdb.cursors
import sys


class BookPipeline(object):
    def __init__(self):
        db = MySQLdb.connect(host='localhost', user='mcrn46', passwd='mcrn46', db='web_mining', charset='utf8',
                             use_unicode=True)

        self.c = db.cursor()
        self.c.connection.autocommit(True)


    def process_item(self, item, spider):
        try:
            self.c.execute("""INSERT INTO books (title,yayinevi,summary,language,year,img,price)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                           (item['title'],
                           item['yayinevi'],
                           item['summary'],
                           item['language'],
                           item['date'],
                           item['images'][0]['path'],
                           item['price'],
                           ))
						   
            self.c.execute("""INSERT INTO authors (name)
                        VALUES (%s)""",
                           (item['author'],
                           ))
						   
            self.c.execute("""INSERT INTO genres (genre)
                        VALUES (%s)""",
                           (item['genre'],
                           ))

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)

        return item