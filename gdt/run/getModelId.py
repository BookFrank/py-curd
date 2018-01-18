#! /usr/bin/env python
# -*- coding: utf-8 -*-
"demo数据同步流程"
__author__ = "liyang"
from gdt.dao.CampaignDao import CampaignDao

# def updateAllCampaign(self):
    #     # 1, 调Api层获得campaign列表
    #     campList = self.CampApi.getAllCampaign()
    #     # 2, 调Dao层完成数据入库
    #     flag = self.CampDao.saveAllCampaign(campList)
    #     # 3, 成功or失败
    #     if  flag:
    #         self.logger.info("更新所有推广计划成功")
    #     else:
    #         self.logger.info("更新推广计划失败")

# with open("/Users/lina/Desktop/autoprice.txt", "rw+") as fr:
#     lines = fr.readline(2)
#     print lines

fr = open("/Users/lina/Desktop/autoprice.txt", "rw+")
lines = fr.readlines()
fr.close()

cam = CampaignDao()
for line in lines:
    line = line.split("\t")
    print cam.getId(line[1])
    print line[1]