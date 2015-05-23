#!/usr/bin/env python
#coding:utf-8
import os
import xlrd
import time,datetime
#t=int(time.mktime(datetime.datetime(2015,04,13,0,0,0).timetuple()))
n=int(time.mktime(datetime.datetime(2015,04,27,0,0,0).timetuple()))
n2=int(time.mktime(datetime.datetime(2015,05,05,0,0,0).timetuple()))
n3=int(time.mktime(datetime.datetime(2015,04,26,0,0,0).timetuple()))
import MySQLdb

try:  
   conn_src=MySQLdb.connect(host="115.29.228.53",user="root", passwd="2Ls56VwEK2wUuYDV",port=4453,db="gaodun",charset="utf8" )
except MySQLdb.Error as e:  

  print('connect fails!{}'.format(e))  

conn_src.set_character_set('utf8')

cursor = conn_src.cursor()


#t2=t + 86400
#print(t)

subject={1:{'会计基础':28},2:{'财经法规':29},3:{'会计电算化':30},4:{'初级职称':48},5:{'初级会计实务':130},6:{'经济法基础':131},\
         7:{'中级职称':49},8:{'中级会计实务':132},9:{'经济法':133},10:{'财务管理':134},11:{'审计':36},12:{'会计':37},13:{'税法':38},14:{'经济法':39},15:{'财务管理':45},16:{'战略风险':46}}
for num in subject:
    subject_id=subject[num]
    #print num
    for subject_key in subject_id:
        subject_id=subject_id[subject_key]
        
        student_sql2='SELECT count(distinct(student_id)) FROM `gd_paper_data` WHERE isdel=0 and subject_id=%s  and %s < regdate and regdate < %s '  % (subject_id,n,n2)
        #print(student_sql)
        cursor.execute(student_sql2)
        student_count2=cursor.fetchall()
        if  student_count2:
            student_count2=student_count2[0][0]
        else:
            student_count2=0
        print "一月%s的做题人数是:" % subject_key ,student_count2    



for num in subject:
    subject_id=subject[num]
    #print num
    for subject_key in subject_id:
        subject_id=subject_id[subject_key]
        student_sql2='select (SELECT count(distinct(student_id)) from gd_paper_data  where isdel=0  and subject_id=%s and regdate < %s)-(select count(distinct(student_id)) from  `gd_paper_data` WHERE isdel=0 and subject_id=%s  and regdate < %s ) from `gd_paper_data` WHERE isdel=0  AND subject_id=%s  and  %s < regdate and regdate < %s'  % (subject_id,n2,subject_id,n,subject_id,n,n2)
       #print(student_sql2)
        cursor.execute(student_sql2)
        student_count2=cursor.fetchall()
        if  student_count2:
            student_count2=student_count2[0][0]
        else:
            student_count2=0
        print "一月%s的新增人数是:" % subject_key ,student_count2    






