#!/usr/bin/env python
# coding=utf-8
import tornado.web,time,json,hashlib
import time
from tornado import gen
from bson.objectid import ObjectId
import db
from base import BaseHandler
try: 
    from cStringIO import StringIO
except:
    from StringIO import StringIO

class Register(BaseHandler):
    """
    注册用户
    """
    """
    error status:
    -1 : 输入的验证码不匹配
    -2 : 密码长度太短
    -3 : 该用户名已经被使用
    """
    def get(self):
        error = self.get_argument("error","0")
        self.render("register.html",error = error)

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self):
        username = self.get_argument("username","")
        password = self.get_argument("password","")
        repassword = self.get_argument("repassword","")
        #两次输入的验证码不匹配
        if password != repassword:
            self.redirect("/register?error=-1")
        #密码长度太短
        if len(password) < 5:
            self.redirect('/register?error=-2')
        #该用户名已经被使用
        user = db.con.user.find_one({'username':username})
        if user:
            self.redirect('register?error=-3')
        #插入用户信息
        uinfo = {
            "_id":ObjectId(),
            "username":username,
            "password":password,
            "email":"",
            "qq":"",
            "register_time":time.time(),
            "login_ip":"",
            "login_time":"",
        }
        db.con.user.insert(uinfo)
        self.redirect('/login')

class Login(BaseHandler):
    #登录页面
    def get(self):
        self.render('login.html')

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self):
        username = self.get_argument('username',"")
        password = self.get_argument('password',"")
        uinfo = db.con.user.find_one({'username':username,'password':password})
        if uinfo:
            self.set_cookie('username',username)
            self.redirect('/')
        else:
            error = "username or password is wrong!"
            self.redirect("/login?error=error")

class UnLogin(BaseHandler):
    def get(self):
        self.clear_cookie('username')
        #print self.get_cookie('username')
        #time.sleep()
        self.redirect('/')
        #self.render('Index.html')

