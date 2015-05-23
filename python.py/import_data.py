#!/usr/local/bin/python
# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb
import pymssql
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )

conn_src=MySQLdb.connect(host="192.168.0.15",user="91money",passwd="789789",db="jrd",charset="utf8")
conn_src.set_character_set('utf8')

class Buffer(object):
    MAXSIZE = 819200
    def __init__(self, conn, sql,char="utf8"):
        self.conn = conn
        self.sql = sql
        self.buffer = []
    def append(self, data):
        self.buffer.append(data)
        if len(self.buffer) > self.MAXSIZE:
            self.flush()
    def flush(self):
        data, self.buffer = self.buffer, []
        curr = self.conn.cursor()
        curr.executemany(self.sql, data)
        self.conn.commit()


 
conn_store=pymssql.connect(host="192.168.1.60",user="sa", password="tyclbtF7.",database="JRD",charset="utf8" )
# here are your code for init database connect conn_src and conn_store...

buff = Buffer(conn_store, "insert into UserInfo(id,nickname,mobile,city,city_id,income,name)  values (%s,%s,%s,%s,%s,%s,%s)")
sql_query = {'charset': 'utf8'}
sql_query ="select u.id,u.nickname,u.mobile,u.city,u.city_id,u.income,d.name from user u left join dict d on u.industry = d.id where income > 50"
curr_src = conn_src.cursor()
curr_src.execute(sql_query)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'Table User insert into success'




buff = Buffer(conn_store, "insert into consultant_static  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
Sql_query = {'charset': 'utf8'}
Sql_query ="select  *  from consultant_static"
curr_src = conn_src.cursor()
curr_src.execute(Sql_query)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'table Consultant_static insert into success'

buff = Buffer(conn_store, "insert into user_static  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
Sql_Query_UserStatic = {'charset': 'utf8'}
Sql_Query_UserStatic ="select  *  from user_static"
curr_src = conn_src.cursor()
curr_src.execute(Sql_Query_UserStatic)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'table user_static insert into success'


buff = Buffer(conn_store, "insert into user_consult  values (%s,%s,%s,%s,%s,%s,%s)")
Sql_Query_UserConsult = {'charset': 'utf8'}
Sql_Query_UserConsult ="select  id,user_id,consultant_id,service_type,ctime,reply_num,service_id  from user_consult where is_delete = 0"
curr_src = conn_src.cursor()
curr_src.execute(Sql_Query_UserConsult)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'table user_consult insert into success'


buff = Buffer(conn_store, "insert into user_reserve  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
Sql_Query_UserRserve = {'charset': 'utf8'}
Sql_Query_UserRserve ="select  id,org_id,user_id,service_id,service_type,consultant_id,reserve_time,reserve_num,status,ctime,amount from user_reserve where is_delete = 0"
curr_src = conn_src.cursor()
curr_src.execute(Sql_Query_UserRserve)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'table user_reserve insert into success'



buff = Buffer(conn_store, "insert into org_static  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
Sql_Query_Org = {'charset': 'utf8'}
Sql_Query_Org ="select  * from org_static"
curr_src = conn_src.cursor()
curr_src.execute(Sql_Query_Org)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'table org_static insert into success'
