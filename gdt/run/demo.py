#! /usr/bin/env python
# -*- coding: utf-8 -*-
"demo数据同步流程"
__author__ = "liyang"
from gdt.api.CampaignApi import CampaignApi
from gdt.dao.CampaignDao import CampaignDao
from gdt.helper.Logger import Logger

class Demo(object):

    def __init__(self, confPath):
        self.logger = Logger("Campaign","../log/campaign.log")
        self.CampApi = CampaignApi(confPath)
        self.CampDao = CampaignDao()

    def updateAllCampaign(self):
        # 1, 调Api层获得campaign列表
        campList = self.CampApi.getAllCampaign()
        # 2, 调Dao层完成数据入库
        flag = self.CampDao.saveAllCampaign(campList)
        # 3, 成功or失败
        if  flag:
            self.logger.info("更新所有推广计划成功")
        else:
            self.logger.info("更新推广计划失败")
