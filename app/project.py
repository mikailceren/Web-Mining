#-*- coding: utf-8 -*-
import web
import numpy as np
urls = (
    '/', 'index',
    '/chart', 'charts',
	'/chart2', 'charts2',
	'/chart3', 'charts3',
    '/about', 'about_page',        
    '/book/(.*)/(.*)', 'book',
    '/book/add', 'add_book',
    '/books', 'book_list',            
    '/ebook', 'ebook_list',    
    '/contact', 'contact_page',
    '/genres', 'genre_list',
    '/genre/add', 'add_genre',
    '/shops', 'shop_list',
    '/yayinevi', 'yayinevleri',
    '/authors', 'author_list',
    '/yazarlar', 'yazarlar',
    '/life/(.*)/(.*)', 'yazar',
    '/author/add', 'add_author',
    '/kategori', 'kategoriler',	
    
    
    
)
render = web.template.render('templates/',base="base")
db = web.database(dbn='mysql',user='mcrn46',db='web_mining',pw='mcrn46')

def required(input_str):
   """ Validator """
   input_str = clean_str(input_str)   
   return input_str != ""            

def clean_str(input_str):
   result = input_str.strip()
   words = result.split()
   words = [ w.capitalize() for w in words ]
   result = " ".join(words)
   return(result)

def is_float(input_str):
  try:
    result = float(input_str)
    return True
  except ValueError:
    return False

class index:
    def GET(self):       
        return render.index()

class book_list:
    def GET(self):       
       books = db.select("books")
       authors = db.select("authors")
       authors_aid = {}
       for author in authors:
          authors_aid[author.aid] = author.name
       print "AUTHORS: %s" % authors_aid  
       return render.books(books, authors_aid)


class book:   
    def GET(self, book_name, book_id):
       bid = int(book_id)
       print "BID=%d" % bid
       book = db.select("books", where="bid=$bid", vars=locals())[0]
       aid = book.aid
       author = db.select("authors", where="aid=$aid", vars=locals())[0]             
       from urllib import quote_plus
       return render.book(book, author, quote_plus)

class author_list:
    def GET(self):       
       authors = list(db.select("authors"))
       genres = list(db.select("genres"))
       books = db.select("books")       
       inp = web.input()
       author_books = []
       genre_books = []
       author = inp.get("author", None)
       genre = inp.get("genre", None)        
       if author and genre != None:
           author_name = author.replace("+", " ")
           genre_genre = genre.replace("+", " ")
           author_books = db.query("SELECT * FROM books AS b, authors AS a, genres AS g WHERE a.name = $author_name AND a.aid = b.aid AND g.genre = $genre_genre AND g.gid = b.gid", vars=locals())
       authors_aid = {}
       for author in authors:
          authors_aid[author.aid] = author.name
       print "AUTHORS: %s" % authors_aid   
       return render.authors(authors_aid, genres, authors, author_books)
       
    def old_GET(self):       
       authors = list(db.select("authors"))
       books = db.select("books")
       inp = web.input()
       author_books = []
       author = inp.get("author", None)
       if author != None:
           author_name = author.replace("+", " ")
           print "AUTHOR NAME : %s" % author_name
           for author in authors:
              if author.name == author_name:
                 aid = author.aid
           print "aid : %s" % aid      
           books = db.select("books")
           for book in books:       
               if book.aid == aid:  
                   author_books.append(book)
       
       print "AUTHOR BOOKS : %s" % author_books                        
       return render.authors(authors, author_books)

class yazarlar:
     def GET(self):       
       books = db.select("books")
       authors = db.query("SELECT * FROM authors ORDER BY aid", vars=locals())
       return render.yazarlar(books, "Books", authors)
      
class yazar:   
    def GET(self, book_name, book_id):
       aid = int(book_id)
       #print "BID=%d" % bid
       book = db.select("books", where="aid=$aid", vars=locals())[0]
       aid = book.aid
       author = db.select("authors", where="aid=$aid", vars=locals())[0]             
       from urllib import quote_plus
       return render.life(book, author, quote_plus)
      

class genre_list:
    def GET(self):       
       genres = list(db.select("genres"))
       books = db.select("books")
       authors = db.select("authors")
       inp = web.input()
       genre_books = []
       genre = inp.get("genre", None)
       if genre != None:
           genre_genre = genre.replace("+", " ")
           genre_books = db.query("SELECT * FROM books AS b, genres AS g WHERE g.genre = $genre_genre AND g.gid = b.gid", vars=locals())
       authors_aid = {}
       for author in authors:
          authors_aid[author.aid] = author.name
       #print "AUTHORS: %s" % authors_aid
       return render.genres(authors_aid, genres, genre_books)
       
    def old_GET(self):       
       genres = list(db.select("genres"))
       books = db.select("books")
       inp = web.input()
       genre_books = []
       genre = inp.get("genre", None)
       if genre != None:
           genre_genre = genre.replace("+", " ")
           print "GENRE : %s" % genre_genre
           for genre in genres:
              if genre.genre == genre_genre:
                 gid = genre.gid
           print "gid : %s" % gid      
           books = db.select("books")
           for book in books:       
               if book.gid == gid:  
                   genre_books.append(book)
       
       print "GENRE BOOKS : %s" % genre_books                        
       return render.genres(genres, genre_books)

class shop_list:
      def GET(self):            
          books = db.select("books")        
          return render.shops(books)

class yayinevleri:
   def GET(self):           
       books = db.query("SELECT DISTINCT yayinevi FROM books ORDER BY yayinevi", vars=locals())       
       return render.yayinevi(books)


class ebook_list:
     def GET(self):       
       books = db.select("books")
       authors = db.select("authors")
       authors_aid = {}
       for author in authors:
          authors_aid[author.aid] = author.name
       print "AUTHORS: %s" % authors_aid  
       return render.ebook(books, authors_aid)

class kategoriler:
    def GET(self):
        return render.kategori()

class add_author:
    required_field = web.form.Validator(' Boş bırakılamaz!', required)

    def check_author(name):
       author_rows = list(db.select("authors"))
       author_names = [ a.name for a in author_rows]
       name = clean_str(name)       
       return not name in author_names

    login = web.form.Form(
                         
          web.form.Textbox('name',
            
             web.form.Validator(' Boş bırakılamaz!', required),
             web.form.Validator(' Yazar zaten var!', check_author),
             size=15,
             description="Yazar Adı: "),
          web.form.Textarea('life',
             web.form.Validator(' Boş bırakılamaz!', required),
             rows=5, cols=20,
             description="Hayatı: "),
           
    )
    
           
    def GET(self):   
        form = self.login()
        return render.author_add(form.render())

    def POST(self):   
       
        form = self.login() 
        if not form.validates():
            form.name.value = clean_str(form.name.value)
            return render.author_add(form.render())
        else:    
           form.name.value = clean_str(form.d.name)           
           # new_bid = db.insert('books', title=form.d.title, summary=form.d.summary,
           #                     price=form.d.price, aid=form.d.aid)           
           new_aid = db.insert('authors', **form.d)                       
           raise web.seeother('/yazarlar')
           # return ("Something posted: %s" % inp)
          
class add_book:
    
    author_rows = list(db.select("authors"))
    authors = [ (row.aid, row.name) for row in author_rows ]
    genre_rows = list(db.select("genres"))
    genres = [ (row.gid, row.genre) for row in genre_rows ]
    required_field = web.form.Validator(' Boş bırakılamaz!', required)
    check_year = web.form.Validator(' Lütfen sayı girin!', is_float)
    check_pos = web.form.Validator(' Yıl pozitif olmalı!', lambda s: float(s) > 0)
    
    def check_author_books(inp):
      aid = inp.aid
      title = clean_str(inp.title)
      author_book_rows = db.query("SELECT b.title FROM books AS b WHERE b.aid = $aid", vars=locals())
      author_book_titles = [ row.title for row in author_book_rows ]
      return title not in author_book_titles
    
    book_add_form = web.form.Form( 
      web.form.Textbox('title', required_field, description="Başlık: "),
      web.form.Textarea('summary', required_field, rows="5", cols="20", description="Özet: "),
      web.form.Textbox('yayinevi', required_field, description="Yayınevi: "),
      web.form.Textbox('price', check_year, check_pos, description="Fiyatı: "),
      web.form.Dropdown('aid', authors, description="Yazar: "),  
      web.form.Textbox('year', check_year, check_pos, description="Yayın Yılı: "),
      web.form.Dropdown('gid', genres, description="Türü: "),
      validators = [ web.form.Validator(" Yazarın o kitabı mevcut!", check_author_books) ]                                      
    )
    def GET(self):
       form = self.book_add_form()
       return render.add_book(form.render())  

    def POST(self):  
        form = self.book_add_form()
        if not form.validates():            
            return render.add_book(form.render())
        else:  
           # store new book in DB    
           form.title.value = clean_str(form.d.title)           
           # new_bid = db.insert('books', title=form.d.title, summary=form.d.summary,
           #                     price=form.d.price, aid=form.d.aid)           
           new_bid = db.insert('books', **form.d)
           raise web.seeother('/book/%s/%d' % (form.d.title.replace(" ", "_"), new_bid))
      
class about_page:
    def GET(self):        
        return render.about()

class contact_page:
    def GET(self):
        return render.contact()

class charts:
    def GET(self):       
        return render.chart()

class charts2:
    def GET(self):       
        return render.chart2()
		
class charts3:
    def GET(self):       
        return render.chart3()

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 1234))

