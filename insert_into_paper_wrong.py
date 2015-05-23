#!/usr/bin/env python
import time, MySQLdb
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
TABLES={}
TABLES['Book']="""
    create table book(
        id int(11) auto_increment primary key,
        bookname varchar(20) not null,
        price int(11) not null
    )
"""

try:  

  conn_src=MySQLdb.connect(user='root',passwd='gdmysql_268',host='192.168.21.221',db='gaodun')  

except MySQLdb.Error as e:  

  print('connect fails!{}'.format(e))  

conn_src.set_character_set('utf8')

class Buffer(object):
    MAXSIZE = 81950000000
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
    def len(self):
        print len(self.buffer)
 
conn_store=MySQLdb.connect(host="192.168.21.219",user="root", passwd="password",db="gaodun1",port=3307,charset="utf8" )
# here are your code for init database connect conn_src and conn_store...


buff = Buffer(conn_store, "insert into gd_paper_wrong(`type`,`student_id`,`item_id`,`subject_id`,`project_id`,`regdate`,`modifydate`,`status`,`isdel`)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
sql_query = {'charset': 'utf8'}
sql_query ="select `type`,`student_id`,`item_id`,`subject_id`,`project_id`,`regdate`,`modifydate`,`status`,`isdel` from gd_paper_wrong where id <= 200000"
curr_src = conn_src.cursor()
curr_src.execute(sql_query)
for row in curr_src:
    buff.append(row)
buff.flush()
print 'Table User insert into success'


mnum=0
xnum=200000
for i in range(1,12):
    mnum+=200000
    xnum+=200000
    print (mnum)
    print (xnum)
    buff = Buffer(conn_store, "insert into gd_paper_wrong(`type`,`student_id`,`item_id`,`subject_id`,`project_id`,`regdate`,`modifydate`,`status`,`isdel`)  \
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    sql_query = {'charset': 'utf8'}
    sql_query ="select `type`,`student_id`,`item_id`,`subject_id`,`project_id`,`regdate`,`modifydate`,`status`,`isdel` from gd_paper_wrong  where id <= '%d' and id > '%d'" %(xnum,mnum)
    curr_src = conn_src.cursor()
    curr_src.execute(sql_query)
    for row in curr_src:
        buff.append(row)
    buff.len()
    buff.flush()
    print 'Table User insert into success'
 
