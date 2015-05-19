#!/usr/bin/env python
# coding=utf-8
import tornado.web,time,json,hashlib
import time
from tornado import gen
from bson.objectid import ObjectId
import db
from base import BaseHandler
from datetime import datetime,timedelta
try: 
    from cStringIO import StringIO
except:
    from StringIO import StringIO

class NewArticle(BaseHandler):
    """
    增加一篇文章
    """
    def get(self):
        uinfo = self.uinfo
        print uinfo
        self.render('manage_new_article.html',uinfo=uinfo)

    def post(self):
        uid = self.get_argument('uid')
        title = self.get_argument('title','')
        content = self.get_argument('content','')
        create_time = time.time()
        data={
            'uid':ObjectId(uid),
            'title':title,
            'content':content,
            'create_time':create_time,
            '_id':ObjectId()
        }
        db.con.article.insert(data)
        print data['_id']
        self.redirect('/article?article_id=%s'%data['_id'])

class Article(BaseHandler):
    """
    文章内容
    """
    def get(self):
        article_id = self.get_argument('article_id')
        print article_id
        res = {}
        ainfo = db.con.article.find_one({'_id':ObjectId(article_id)})
        print ainfo
        uinfo = db.con.user.find_one({'_id':ObjectId(ainfo['uid'])})
        print "uinfo :::"
        print uinfo
        res['create_time'] = datetime.fromtimestamp(ainfo['create_time'])
        res['title'] = ainfo['title']
        res['content'] = ainfo['content']
        res['author'] = uinfo['username']
        self.render('manage_article_detail.html',res=res)

class ArticleList(BaseHandler):
    """
    文章列表
    """
    def get(self):
        uinfo = self.uinfo
        uid = uinfo['_id']
        res = []
        ainfo = db.con.article.find({'uid':ObjectId(uid)})
        for i in ainfo:
            a ={}
            a['create_time'] = datetime.fromtimestamp(i['create_time'])
            a['title'] = i['title']
            a['content'] = i['content'][0:100]
            a['author'] = uinfo['username']
            a['article_id'] = i['_id']
            res.append(a)
        self.render('manage_article_list.html',res=res)

        

