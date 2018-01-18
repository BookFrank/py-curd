#! /usr/bin/env python
# -*- coding: utf-8 -*-
"推广计划数据持久层"
__author__ = "liyang"
from BaseDao import BaseDao

class CampaignDao(BaseDao):

    def saveAllCampaign(self,campaignList):
        num = self.db.insertMany('rep_gdt_campaign', campaignList)
        if num > 0:
            print "保存成功"
            return True
        else:
            print "保存失败"
            return False

    def getId(self, modelName):
        res = self.db.fetchOne(sql)
        return res
