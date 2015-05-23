#!/bin/env python
# -*- coding: <utf-8> -*-
import MySQLdb
import re

q=re.compile(r'(?<=T).(?![^\d])')

try:  
   conn_src=MySQLdb.connect(host="115.29.228.53",user="root", passwd="2Ls56VwEK2wUuYDV",port=4453,db="gaodun",charset="utf8" )
except MySQLdb.Error as e:  

  print('connect fails!{}'.format(e))  

conn_src.set_character_set('utf8')

cursor = conn_src.cursor()
id_sql="select id from gd_card_code where card_id=108"
cursor.execute(id_sql)
ids=cursor.fetchall()


content_sql="select num from gd_card_code where card_id  = 108"
cursor.execute(content_sql)
contents=cursor.fetchall()

for  connect in contents:
	 c=connect[0]
	 numd=q.sub('2',c)
	 update_sql="update gd_card_code set num ='%s',prefix='T254' where card_id = 108" % (numd)
	 cursor.execute(update_sql)
	 cursor.execute('commit')
	 print(update_sql)


conn_src.close()
