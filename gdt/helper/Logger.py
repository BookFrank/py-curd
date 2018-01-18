#! /usr/bin/env python
# -*- coding: utf-8 -*-
"日志模块封装"
__author__ = "liyang"
import os, logging

class Logger(object):
    def __init__(self, name, logPath, logLevel=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logLevel)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        # 设置文件handler
        fh = logging.FileHandler(logPath)
        fh.setFormatter(fmt)
        fh.setLevel(logLevel)
        self.logger.addHandler(fh)
        # 设置命令行handler
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        ch.setLevel(logLevel)
        self.logger.addHandler(ch)


    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    logger = Logger("GdtSync", "../log/gdt_sync.log")
    logger.info("测试日志")

