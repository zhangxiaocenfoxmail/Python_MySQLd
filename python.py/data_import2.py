#!/bin/env python
# -*- coding: utf-8 -*-     
#mysqldb    
import time, MySQLdb   
import pymssql
import re
import os



   
#连接    
conn=MySQLdb.connect(host="192.168.0.15",user="91money",passwd="789789",db="jrd",charset="utf8")  
cursor = conn.cursor()    
cursor1 = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
cursor4 = conn.cursor()
cursor5 = conn.cursor()
cursor6 = conn.cursor()
cursor7 = conn.cursor()
cursor8 = conn.cursor()



n = cursor.execute("select count(*) from user where is_delete =0")    
for row in cursor.fetchall():    
    for r in row:    
        print r
n1 = cursor1.execute("select count(*) from user where is_delete = 0 and type = 0 and city_id = 22")
for row1 in cursor1.fetchall():
    for r1 in row1:
        print r1

n2 = cursor2.execute("select count(*) from user_reserve where is_delete = 0 and status=3")
for row2 in cursor2.fetchall():
    for r2 in row2:        
        print r2

n3 = cursor3.execute("select count(*) from user_consult where is_delete = 0")
for row3 in cursor3.fetchall():
    for r3 in row3:
        print r3

n4 = cursor4.execute("select count(*) from user where is_delete = 0 and type = 1")
for row4 in cursor4.fetchall():
    for r4 in row4:
        print r4

n5 = cursor5.execute("select count(*) from org where is_delete = 0")
for row5 in cursor5.fetchall():
    for r5 in row5:
        print r5

n6 = cursor6.execute("select count(*) from brand where is_delete = 0")
for row6 in cursor6.fetchall():
    for r6 in row6:
        print r6

n7 = cursor7.execute("select count(*) from user_reserve where is_delete = 0 and status=3")
for row7 in cursor7.fetchall():
    for r7 in row7:
        print r7

cursor.close() 
conn.close()


time.localtime(time.time())
time.strftime('%Y-%m-%d',time.localtime(time.time()))
print time.strftime('%Y-%m-%d',time.localtime(time.time()))


Time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
CountUser = r
CounUserSh  = r1
CountReserve3= r2
CountConsult = r3
CountConsultant = r4
CountOrg = r5
CountBrand = r6
CountReserve = r7
DemandNum = os.popen('python2.7 /home/mysql3.py')
CountDemand = DemandNum.read()
ServiceNum = os.popen('python2.7 /home/mysql2.py')
CountService = ServiceNum.read()


print type(DemandNum)
print type(CountDemand)



db=pymssql.connect(host="192.168.1.60",user="sa", password="tyclbtF7.",database="JRD" )
cursor = db.cursor()
Sql="INSERT INTO jrd_num(CountUser ,CounUserSh ,CountReserve3,CountConsult,CountConsultant,CountOrg,CountBrand,CountReserve,Time,CountDemand,CountService)    VALUES('%d','%d','%d','%d','%d','%d','%d','%d','%s','%s','%s')" % (CountUser ,CounUserSh ,CountReserve3,CountConsult,CountConsultant,CountOrg,CountBrand,CountReserve,Time,CountDemand,CountService)
try:
    cursor.execute(Sql)
    db.commit()
except:
    db.rollback()
db.close()
cursor.close()
