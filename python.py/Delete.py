# -*- coding: utf-8 -*- 
#coding = utf-8
#!/usr/bin/evn python    
#mysqldb    
import time, MySQLdb
import pymssql
import re
import os

class MSSQL(object):
	
	def __init__(self,conn,Sql,char="utf8"):
		self.conn = conn
		self.Sql = Sql

	def  flush(self):
		curr = self.conn.cursor()
		curr.executemany(self.Sql)
		self.conn.commit()
		
conn_store=pymssql.connect(host="192.168.1.60",user="sa", password="tyclbtF7.",database="JRD" )

Sql_Delete="delete from user_static"
SqlO_Delete="delete from org_static"
SqlC_Delete="delete from consultant_static"
SqlU_Delete="delete from UserInfo"
SqlCounsult_Delete="delete from user_consult"
SqlR_Delete="delete from user_reserve"
conn_src = conn_store.cursor()

try:
    conn_src.execute(SqlC_Delete)
    conn_src.execute(SqlR_Delete)
    conn_src.execute(SqlCounsult_Delete)
    conn_src.execute(SqlU_Delete)
    conn_src.execute(SqlO_Delete)
    conn_src.execute(Sql_Delete)
    conn_store.commit()
except Exception as d:
    print d
else:
    print 'Table data clear'
    conn_store.close()
    conn_src.close()

