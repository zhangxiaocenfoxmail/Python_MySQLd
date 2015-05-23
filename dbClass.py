#!/usr/bin/env python3
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, sys
import mysql.connector as mysql

class DbConnect(object):

    """
        Use server [ tk | server | bd_tongji | test | www | tkjz | tkys ] only!
    """

    def __init__(self, server=None):
        self.port = 3306
        self.charset = 'utf8'
        if server == 'tk':
            self.host = 'm.gaodun.com'
            self.db = 'tk_source'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'tk_2014':
            self.host = 'm.gaodun.com'
            self.db = 'tk_source_2014'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'tk_2015':
            self.host = 'm.gaodun.com'
            self.db = 'tk_source_2015'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'server':
            self.host = '192.168.21.220'
            self.db = 'sms'
            self.user = 'wangning'
            self.passwd = 'gdmysql_268'
        elif server == 'www':
            self.host = '120.26.62.94'
            self.db = 'gaodun'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4453
        elif server == 'www_dede':
            self.host = '120.26.62.94'
            self.db = 'db_dedecms'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4453
        elif server == 'www_ucenter':
            self.host = '120.26.62.94'
            self.db = 'db_ucenter'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4453
        elif server == 'www_bbs':
            self.host = '120.26.62.94'
            self.db = 'w_bbs_gaodun'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4453
        elif server == 'www_im':
            self.host = '120.26.62.94'
            self.db = 'db_im'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4453
        elif server == 'local_test':
            self.host = '127.0.0.1'
            self.db = 'test'
            self.user = 'root'
            self.passwd = 'wn8197529'
        elif server == 'local_mysql':
            self.host = '127.0.0.1'
            self.db = 'mysql'
            self.user = 'root'
            self.passwd = 'wn8197529'
        elif server == 'bd_tongji':
            self.host = '192.168.21.220'
            self.db = 'bd_tongji'
            self.user = 'wangning'
            self.passwd = 'gdmysql_268'
        elif server == 'test':
            self.host = 'm.gaodun.com'
            self.db = 'gaodun'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'yun':
            self.host = '120.26.62.94'
            self.db = 'gaodun'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
            self.port = 4306
        elif server == 'tkjz':
            self.host = 'm.gaodun.com'
            self.db = 'tkjz_source'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'tkys':
            self.host = 'm.gaodun.com'
            self.db = 'tkys_source'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'zhaopin':
            self.host = 'm.gaodun.com'
            self.db = 'db_zhaopin'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'realzhaopin':
            self.host = '121.40.133.124'
            self.db = 'db_zhaopin'
            self.user = 'zhaopin'
            self.passwd = '2Ls56VwEK2wUuYDV'
        elif server == 'kj':
            self.host = 'm.gaodun.com'
            self.db = 'gd_kjapp'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'newkj':
            self.host = 'm.gaodun.com'
            self.db = 'gd_new_kjapp'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'realkj':
            self.host = '121.40.133.124'
            self.db = 'gd_kjapp'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
        elif server == 'test_test':
            self.host = 'm.gaodun.com'
            self.db = 'test'
            self.user = 'root'
            self.passwd = 'gdmysql_268'
        elif server == 'tongji':
            self.host = '112.124.23.158'
            self.db = 'db_tongji'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
        elif server == 'tongji_laoshi':
            self.host = '112.124.23.158'
            self.db = 'db_laoshi'
            self.user = 'root'
            self.passwd = '2Ls56VwEK2wUuYDV'
        else:
            self.host = '192.168.21.220'
            self.db = 'gaodun'
            self.user = 'root'
            self.passwd = 'gdmysql_268'

    def dbconn(self):
        self.conn = mysql.connect(host=self.host, db=self.db, user=self.user, passwd=self.passwd, port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()
        return self.cursor

    def conn(self):
        conn = mysql.connect(host=self.host, db=self.db, user=self.user, passwd=self.passwd, port=self.port, charset=self.charset)
        return conn
