#!/bin/env python
# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        txt2xls.py
# Purpose:     处理SQL生成Excel
# Author:      zhoujy
# Created:     2013-01-11
# update:      2013-01-11
# Copyright:   (c) Mablevi 2013
# Licence:     zjy
# Usage:       python txt2xls.py 生成的excel名字
#-------------------------------------------------------------------------------
import paramiko
import MySQLdb
import datetime
import os
import sys
import xlwt
import getpass

def get_data(conn,query): #从MySQL取数据,导成文本
    query = query + " into outfile '/home/zhoujy/outfile/out.txt'"
    cursor = conn.cursor()
    cursor.execute(query)

def sync_txt(hostname,port,username,password): #同步下载文本
    local_dir=r'/home/zhoujy/outfile/'
    remote_dir=r'/home/zhoujy/outfile/' 
    try :
        t=paramiko.Transport((hostname,port))          
        t.connect(username=username,password=password)          
        sftp=paramiko.SFTPClient.from_transport(t)  
#        files=sftp.listdir(dir_path)          
        files=sftp.listdir(remote_dir)          
        for f in files:
            print ''               
            print '#########################################'                  
            print 'Beginning to download file  from %s  %s ' % (hostname,datetime.datetime.now().strftime('%H:%M:%S'))                
            print 'Downloading file:',os.path.join(remote_dir,f) 
            sftp.get(os.path.join(remote_dir,f),os.path.join(local_dir,f))#下载               
#            sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f)) 上传                 
            print 'Download file success %s ' % datetime.datetime.now().strftime('%H:%M:%S')        
            print '##########################################'   
        t.close()
    except Exception :  
        print "connect error!" 

def rm_txt(hostname,port,username,password): #在服务器上执行删除文本
    paramiko.util.log_to_file('paramiko.log')
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())          
    s.connect(hostname = hostname,port=port,username=username, password=password)          
    stdin,stdout,stderr=s.exec_command('rm /home/zhoujy/outfile/out.txt')          
    print stdout.read()       
    s.close()

def txt2xls(filename,xlsname):  #文本转换成xls
    print 'converting xls ... '
    f = open(filename)
    x = 0
    y = 0
    xls=xlwt.Workbook()
    sheet = xls.add_sheet('sheet1',cell_overwrite_ok=True)
    while True:
        line = f.readline()
        if not line:
            break
        for i in line.split('\t'):
            item=i.strip().decode('utf8')
            sheet.write(x,y,item)
#            xls.save('test.xls')
            y += 1
        x += 1
        y = 0
    f.close()
    xls.save(xlsname+'.xls')

if __name__ == '__main__':
    hostname=raw_input('Enter Host IP   : ')
    port = input('Enter Host port : ')
    username=raw_input('Enter Host User : ')
    password = getpass.getpass('Enter Host Pwd  : ')
    Mport = input('Enter MySQL port : ')
    DBName = raw_input('Enter MySQL DBName: ')
    query = raw_input('Press SQL : ')
    conn = MySQLdb.connect(host=hostname,user='root',passwd='redhat',charset='utf8',db=DBName,port=Mport)
    get_data(conn,query)
    sync_txt(hostname,port,username,password)
    rm_txt(hostname,port,username,password)
    txt2xls('out.txt',sys.argv[1])
    raw_input('按回车结束')
