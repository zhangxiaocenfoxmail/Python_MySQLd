#!/usr/bin/env python
#coding=utf-8
  
def num(*num):  
        #遍历参数列表，判断参数类型是否为整形  
        for i in num:  
                if not isinstance(i,int):  
                        return '参数错误,参数必须为整数'  
        return max(num),min(num)  
	print num()
	return num()  
num(124232,1234,23,42,3,1,23,123,23,123123,123123)  


"""
def Str(*sen):
	for i in sen:
		if not isinstance(i,str):
			return "输入的参数必须为字符串"
	a = sorted(sen,key=lambda k:len(k))
	return "Maxnum is %d and Minnum is %d" %(len[a-1],len(a[0]))
Str('zhangjin','xushi','dinghongwu','1242o1i3u1oi2hroi1h2wo12ihe1oihe')
"""

import os
def get_doc(module):
	a='pydoc %s' %module
	m=os.popen(a).read()
	return m



def get_txt(f):
	a='cat %s' %f
	m = os.popen(a).read()
	return m 

get_txt('/etc/passwd')

