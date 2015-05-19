#!/usr/bin/env python
# coding=utf-8
import tornado.ioloop
import tornado.web,tornado.options
import db
import tornado.web,json,os,time,re
from base import BaseHandler
import auth
import userback

class Index(BaseHandler):
    def get(self):
        self.render("Index.html")

application = tornado.web.Application([
    (r'/',Index),
    (r'/login',auth.Login),
    (r'/unlogin',auth.UnLogin),
    (r'/register',auth.Register),
    (r'/newarticle',userback.NewArticle),
    (r'/article',userback.Article),
    (r'/articlelist',userback.ArticleList),
    
    ],
    debug = True,
    template_path=os.path.join(os.path.dirname(__file__), "templates")
)

if __name__ == "__main__":
    try:
        db.init()
        print "mongo start"
        application.listen(8888)
        print "start port 8888"
        tornado.ioloop.IOLoop.instance().start()
    except:
        print "error"
        import traceback
        print traceback.print_exc()

