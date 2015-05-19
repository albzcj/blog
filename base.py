#!/usr/bin/env python
# coding=utf-8
import tornado.web,json,os,time,re
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import logging
from bson.json_util import dumps,loads
import base64
import json
from tornado.log import access_log,app_log,gen_log
import traceback
import db

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        #根据cookies生成用户信息
        access_log.info('>>>>>>>>>>>>>>>>>>>>>>>')
        username = self.get_cookie('username','')
        uinfo = db.con.user.find_one({'username':username})
       # print username
        self.uinfo = uinfo
        if username:
            pass

    
    def render(self,template_name,**kwargs):
        kwargs['uinfo'] = self.uinfo
        return super(BaseHandler,self).render(template_name,**kwargs)

    def redirect(self,url):
        return super(BaseHandler,self).redirect(url)
