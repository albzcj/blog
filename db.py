#!/usr/bin/env python
# coding=utf-8
import pymongo
con = None

def mongo_init():
    #初始化mongodb
    global con
    myclient = pymongo.Connection("localhost", 27017)
    con = myclient['myblog']
    

def init():
    mongo_init()

if __name__ == "__main__":
    init()
    print "db start!"


