#! /usr/bin/env python
# -*- coding: utf-8 -*-
'本模块为API基础类'
__author__ = 'liyang'
import ConfigParser
import time,hashlib,base64

class BaseApi(object):

    def __init__(self, confPath):
        cf = ConfigParser.ConfigParser()
        cf.read(confPath)
        self.app_id = cf.get("gdt", "app_id").strip()
        self.app_key = cf.get("gdt", "app_key").strip()
        self.token = self.getToken()

    # 组装token
    # @param app_id, app_key
    # @return token
    def getToken(self):
        timestamp = str(int(time.time()))
        sign = hashlib.sha1(self.app_id + self.app_key + timestamp).hexdigest()
        token = base64.b64encode(self.app_id + "," + self.app_id + "," + timestamp + "," + sign)
        return token


if __name__ == '__main__':
    baseApi = BaseApi("../conf/hmc.conf")
    print "Token值为-->", baseApi.token