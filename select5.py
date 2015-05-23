#!/usr/bin/env python
#coding:utf-8
import os
import xlrd
import time,datetime
#t=int(time.mktime(datetime.datetime(2015,04,13,0,0,0).timetuple()))
n=int(time.mktime(datetime.datetime(2015,04,27,0,0,0).timetuple()))
n2=int(time.mktime(datetime.datetime(2015,05,05,0,0,0).timetuple()))
n3=int(time.mktime(datetime.datetime(2015,04,12,0,0,0).timetuple()))
import MySQLdb
try:  
   conn_src=MySQLdb.connect(host="115.29.228.53",user="root", passwd="2Ls56VwEK2wUuYDV",port=4453,charset="utf8" )
except MySQLdb.Error as e:  

  print('connect fails!{}'.format(e))  

conn_src.set_character_set('utf8')

cursor = conn_src.cursor()


paper_student_id="select  GROUP_CONCAT(DISTINCT(gaodun.gsi.student_id)) from gaodun.gd_members_student_info gsi where gaodun.gsi.student_id in (select gw.student_id from gaodun.gd_paper_wrong gw  where gw.project_id = 5)"
#print (paper_student_id)
cursor.execute(paper_student_id)
paper_student_count2=cursor.fetchall()
paper_student_count3=paper_student_count2[0][0]
#print (paper_student_count3)
paper_student_count4="select   GROUP_CONCAT(DISTINCT(ugm.regip))  from gaodun.gd_members_student  gs join gaodun.gd_members gm on gs.member_id = gm.id join db_ucenter.gd_members ugm on gm.uid = ugm.uid where gs.id in (%s)"  %(paper_student_count3)
cursor.execute(paper_student_count4)
paper_student_count5=cursor.fetchall()
paper_student_ip=paper_student_count5[0][0]
print paper_student_ip