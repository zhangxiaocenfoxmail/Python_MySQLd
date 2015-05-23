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
   conn_test=MySQLdb.connect(host="115.29.228.53",user="root", passwd="2Ls56VwEK2wUuYDV",port=4453,charset="utf8" )
except MySQLdb.Error as e:  

  print('connect fails!{}'.format(e))  

conn_src.set_character_set('utf8')



for i in range(1,3):
    mnum+=200000
    xnum+=200000
    print (mnum)
    print (xnum)
    buff = Buffer(conn_store, "insert into info(qq,uid,session_id,ip,url,title, access_time,bdwords)  \
        values (%s,%s,%s,%s,%s,%s,%s,%s)")
    sql_query = {'charset': 'utf8'}
    sql_query ="select qq,uid,session_id,ip,url,title, access_time,bdwords from info  where id <= '%d' and id > '%d'" %(xnum,mnum)
    curr_src = conn_src.cursor()
    curr_src.execute(sql_query)
    for row in curr_src:
        buff.append(row)
    buff.len()
    buff.flush()
    print 'Table User insert into success'
 
