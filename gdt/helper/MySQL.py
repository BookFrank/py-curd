#! /usr/bin/env python
# -*- coding: utf-8 -*-
'MySQL数据库CURD封装'
__author__ = "liyang"
import sys
import MySQLdb
from gdt.helper.Logger import Logger

class MySQL(object):

    def __init__(self, host, username, password, db_name, port=3306, charset='utf8'):
        self.conn = self.connect(host, username, password, db_name, port, charset)
        self.logger = Logger("MySQL", "../log/mysql.log")

    # 获取MySQL连接对象 liyang
    # @param
    # @return connection
    def connect(self, host, username, password, db_name, port=3306, charset='utf8'):
        try:
            conn = MySQLdb.connect(host, username, password, db_name, port, charset)
            return conn
        except MySQLdb.Error,e:
            self.logger.error("MySQL Connect Error: %s" % e)
            return None

    # 插入一条数据  liyang
    # @param  tableName, dataDict
    # @return insertId
    def insertOne(self, tableName, dataDict):
        if type(dataDict) is dict:  # 字典类型数据,插入一行
            cursor = self.conn.cursor()
            keysList = dataDict.keys()
            keys = "(" + ','.join(keysList) + ")"
            for i in range(len(keysList)):
                keysList[i] = "%(" + keysList[i] + ")s"
            values = "(" + ','.join(keysList) + ")"
            sql = "INSERT INTO " + tableName + keys +" VALUES " + values
            try:
                cursor.execute(sql, dataDict)
                self.conn.commit()
                return self.getLastInsertId(cursor)
            except Exception,e:
                self.conn.rollback()
                self.logger.error("MySQL insertOne Error: %s" % e)
                return None
            finally:
                cursor.close()
        else:
            print "参数有误,只允许字典类型数据"

    # 批量插入数据  liyang
    # @param  tableName,dictList
    # @return affectedRows
    def insertMany(self, tableName, dictList):
        if  type(dictList) is list:
            cursor = self.conn.cursor()
            tupleList = []
            for row in dictList:
                tupleList.append(tuple(row.values()))
            valList = dictList[0].keys()
            keys = ','.join(valList)
            for index, attr in enumerate(valList):
                valList[index] = "%s"
            values = ",".join(valList)
            sql = "INSERT INTO " + tableName + " (" + keys + ")" + " VALUES (" + values + ")"
            try:
                cursor.executemany(sql, tupleList)
                self.conn.commit()
                return self.getAffectedRows(cursor)
            except Exception,e:
                self.conn.rollback()
                self.logger.error("MySQL insertMany Error: %s" % e)
                return None
            finally:
                cursor.close()
        else:
            print "请传入List类型数据"

    # query查询(修改或删除时使用)  liyang
    # @param  sql
    # @return flag (0-失败 1-成功)
    def query(self, sql):
        cursor = self.conn.cursor()
        try:
            flag = cursor.execute(sql)
            self.conn.commit()
            return flag
        except MySQLdb.Error,e:
            self.conn.rollback()
            self.logger.error("MySQL Query Error: %s" % e)
            self.logger.error("sql = %s" % sql)
            return None
        finally:
            cursor.close()

    # 查询一行数据  liyang
    # @param  sql
    # @return dict
    def fetchOne(self, sql):
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            res = cursor.fetchone()
            return res
        except MySQLdb.Error,e:
            self.logger.error("MySQL FetchOne Error: %s" % e)
            self.logger.error("sql = %s" % sql)
            return None
        finally:
            cursor.close()

    # 查询一组数据  liyang
    # @param  sql
    # @return tuple （{dict}, {dict}, {dict}）
    def fetchAll(self, sql):
        cursor = self.conn.cursor(MySQLdb.cursors.DictCursor)
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except MySQLdb.Error,e:
            self.logger.error("MySQL FetchAll Error: %s" % e)
            self.logger.error("sql = %s" % sql)
            return None
        finally:
            cursor.close()

    # 获取最后插入id liyang
    # @param
    # @return id
    def getLastInsertId(self, cursor):
        return cursor.lastrowid

    # 获取影响的行数 liyang
    # @param
    # @return rowcount
    def getAffectedRows(self, cursor):
        return cursor.rowcount

    # 析构方法(关闭连接进程) liyang
    # @param
    # @return
    def __del__(self):
        self.conn.close()


if __name__ == "__main__":
    db = MySQL("192.168.55.199","root","root","hd_huodong")

    fr = open("/Users/lina/Desktop/autoprice.txt", "rw+")
    lines = fr.readlines()
    fr.close()

    for line in lines:
        lineList = line.split("\t")
        sql = "SELECT model_id FROM bitauto_car_models WHERE seo_name = " + "'" + lineList[1] + "'"
        resDict = db.fetchOne(sql)
        if  resDict is None:
            print line
        else:
            print resDict['model_id']
        # print line[1]

    sys.exit(0)

    # rep_test表结构  id, name, age

    # 插入一条数据demo
    oneRow = {'name':'liyang', 'age':25}
    res1 = db.insertOne('rep_test',oneRow)
    print "插入一条数据结果",res1

    # 批量插入数据demo
    rowList = [
        {'name':'frank', 'age':24},
        {'name':'kevin', 'age':23},
        {'name':'angel', 'age':21}
    ]
    res2 = db.insertMany('rep_test',rowList)
    print "批量插入数据结果->",res2

    # 删除数据demo
    delSql = "DELETE FROM rep_test WHERE name = 'kevin'"
    res3 = db.query(delSql)
    print "删除数据结果->",res3

    # 更新数据demo
    updateSql = "UPDATE rep_test SET name = 'liyang_update' WHERE name = 'liyang'"
    res4 = db.query(updateSql)
    print "更新数据结果为->",res4

    # 查询一条数据demo
    fetchOneSql = "SELECT * FROM rep_test where name = 'liyang_update'"
    res5 = db.fetchOne(fetchOneSql)
    print "查询一条结果为->",res5

    # 批量查询数据demo
    fetchAllSql = "SELECT * FROM rep_test"
    res6 = db.fetchAll(fetchAllSql)
    print "批量查询结果为->",res6
