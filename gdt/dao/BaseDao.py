#! /usr/bin/env python
# -*- coding: utf-8 -*-
'数据持久层基础类'
__author__ = "liyang"
from gdt.helper.MySQL import MySQL
import ConfigParser

class BaseDao(object):

    def __init__(self):
        cf = ConfigParser.ConfigParser()
        cf.read("../conf/db.conf")
        host = cf.get("mysql", "host").strip()
        username = cf.get("mysql", "username").strip()
        password = cf.get("mysql", "password").strip()
        db_name = cf.get("mysql", "db_name").strip()
        port = cf.get("mysql", "port").strip()
        charset = cf.get("mysql", "charset").strip()
        # print host,username,password,db_name,port,charset
        self.db = MySQL(host,username,password,db_name,int(port),charset)


if __name__ == "__main__":
    baseDao = BaseDao()
    print "数据库句柄地址-->", baseDao.db