#! /usr/bin/env python
# -*- coding: utf-8 -*-
"推广计划相关Api"
__author__ = "liyang"
import requests
import json
from BaseApi import BaseApi

uri = "http://sanbox.api.e.qq.com/ads/v3/"
url_campaign_select = uri + "campaign/select"


class CampaignApi(BaseApi):

    def __init__(self,confPath):
        super(CampaignApi,self).__init__(confPath)

    # 获得推广计划列表
    # @param
    # @return connection
    def getAllCampaign(self):
        print self.app_id
        url = url_campaign_select
        headers = {"Authorization": "Bearer " + self.token}
        params = {"advertiser_id": self.app_id,
                  "page_size": 100}
        try:
            r = requests.get(url, headers=headers, params=params)
            # print r.content
            resJson = '{"data":{"list":[{"campaign_id":1235935,"campaign_name":"测试的广告计划20  51923","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":5000,"budget_limit_date":0,"created_time":1455877888,"last_modified_time":1455877888,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"},{"campaign_id":1168428,"campaign_name":"测试的广告计划3","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":10002,"budget_limit_date":0,"created_time":1452595980,"last_modified_time":1452650158,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"},{"campaign_id":1168383,"campaign_name":"测试的广告计划","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":5000,"budget_limit_date":0,"created_time":1452594710,"last_modified_time":1452594710,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"}],"page_info":{"page":1,"page_size":10,"total_num":3,"total_page":1}},"code":0,"message":""}'
            resDict = json.loads(resJson)
            if  resDict['code'] == 0 and resDict['data']['page_info']['total_num'] > 0:
                print "success"
                return resDict
            else:
                print "fail"
                return resJson

        except Exception,e:
            print e
            return e






if __name__ == "__main__":
    # cc = CampaignApi("../conf/hmc.conf")
    # cc.getAllCampaign()
    resJson = '{"data":{"list":[{"campaign_id":1235935,"campaign_name":"测试的广告计划20  51923","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":5000,"budget_limit_date":0,"created_time":1455877888,"last_modified_time":1455877888,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"},{"campaign_id":1168428,"campaign_name":"测试的广告计划3","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":10002,"budget_limit_date":0,"created_time":1452595980,"last_modified_time":1452650158,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"},{"campaign_id":1168383,"campaign_name":"测试的广告计划","campaign_type":"CAMPAIGN_TYPE_NORMAL","daily_budget":5000,"budget_limit_date":0,"created_time":1452594710,"last_modified_time":1452594710,"pv_demanded":0,"total_budget":0,"completed_time":0,"speed_mode":"SPEED_MODE_STANDARD","max_impression_include":0,"outer_campaign_id":0,"configured_status":"AD_STATUS_NORMAL","retainability_in_feeds":"NO"}],"page_info":{"page":1,"page_size":10,"total_num":3,"total_page":1}},"code":0,"message":""}'
    resDict = json.loads(resJson)
    print  type(resDict['data']['list']),resDict['data']['list']
    # if resDict['code'] == 0 and resDict['data']['page_info']['total_num'] > 0:
    #     print "success"
    # else:
    #     print "fail"
