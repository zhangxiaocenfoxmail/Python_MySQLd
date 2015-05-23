# encoding: utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb

conn=MySQLdb.connect(host="192.168.0.15",user="91money",passwd="789789",db="jrd",charset="utf8")
cursor = conn.cursor()
n = cursor.execute("select  id  from user where is_delete =0 and income > 1000")  
for row in cursor.fetchall():
    id = row[0]
#    nickname = row[1]
#    mobile = row[2]
#    income = row[3] 
#    print "id=%d,nickname=%s,mobile=%s,income=%s" % (id,nickname,mobile,income)
print id

db = MySQLdb.connect(host="192.168.1.188",user="root",passwd="redhat",db="jrd3" )
cursor1 = db.cursor()

Sql="INSERT INTO user2(id) VALUES (%d)"
for row in cursor.fetchall():
    cursor1.execute(Sql,(row[0]))
db.commit()
db.close()
cursor1.close()
