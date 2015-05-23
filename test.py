#!/bin/env python
# -*- coding: <utf-8> -*-

from mysql.connector import errorcode
##load mode
import mysql.connector

from symbol import except_clause

try:  

  cnn=mysql.connector.connect(user='root',password='',host='127.0.0.1')  

except mysql.connector.Error as e:  

  print('connect fails!{}'.format(e))  


DB_NAME='firefox'
TABLES={}
TABLES['Book']="""
    create table book(
        id int(11) auto_increment primary key,
        bookname varchar(20) not null,
        price int(11) not null
    )
"""

TABLES['People']="""
    create table people(
        id int(11) auto_increment primary key,
        name varchar(20) not null
    )
"""

TABLES['student']="""CREATE TABLE if not exists student (
	`id` int(10) NOT NULL AUTO_INCREMENT,
	`name` varchar(10) DEFAULT NULL,
	`age` int(3) DEFAULT NULL, 
	PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8
"""

#create databse exmaple

cursor=cnn.cursor()

def create_database(cursor):
    try:
        cursor.execute("create database if not exists {} default character set 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print ('create  database:{}'.format(err))
        exit(1)

try:

    cnn.database=DB_NAME

except mysql.connector.Error as err:
	
    if (err.errno==errorcode.ER_BAD_DB_ERROR):
        
        create_database(cursor)

        cnn.database=DB_NAME
    else:
    	print (err)
    	exit(1)


for name,ddl in TABLES.items():

    try:
        cursor.execute(ddl)
    except mysql.connector.Error as err:     
        if(err.errno==errorcode.ER_TABLE_EXISTS_ERROR):
		print ("alredy exits....")
	else:
            print(err.msg)
    else:
        print("successfully...")



"""

insert into databases

"""


try:  

  cnx=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='firefox')  

except mysql.connector.Error as e:  

  print('connect fails!{}'.format(e))  

incursor=cnx.cursor()

def  DataInsert(cursor):
    pass
add_book="""
    insert into book (bookname,price) values(%s,%s)
"""

data_book=('the one',100)


add_people="""
    insert into people (name) values(%s)
"""
data_people=('lazy',)

#insert into daat

incursor.execute(add_book,data_book)
incursor.execute(add_people,data_people)
cnx.commit()
incursor.close()
cnx.close()

cursor.close()
cnn.close()
