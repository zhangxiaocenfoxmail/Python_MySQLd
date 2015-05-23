#!/usr/bin/env python
# -*- coding:utf-8 -*-
def getnum(numLst=[1,2,3,4,5,6,'zhanghui']):
    import math
    lst=[]
    for item in numLst:
	    if isinstance(item,int):
		    pass
	    elif isinstance(item,float):
		    pass
	    elif isinstance(item,long):
		    pass
	    elif isinstance(item,complex):
		    pass
	    else:
		    assert str(item).isdigit(),'number only'
	    if item==0:
	        continue
	    m=item%2
	    if m==0 and (isinstance(m,int) or isinstance(m,long)):
		    lst.append(item);
    print lst
    return lst
getnum(numLst=[1,2,3,4,5,6]);

"""
def getPage(url):
	import urllib
	statusCode = urllib.urlopen(url).getcode()
	return statusCode == 200
if __name__=="__main__":
	result = 0
	url = raw_input("请输入要测试的网址。");
	cut = input("请输入循环的次数");
	for i in range(0,cut):
		if (getPage(url) == True):
				result += 1;
	print('Test' + str(cut) + 'times, succed' + str(result)+'times')

def getPage(url):
    import urllib2
    statusCode = urllib2.urlopen(url).getcode()
    if statusCode == 200:
        try:
            f=urllib2.urlopen(url,timeout = 0.1)
	except urllib2.URLError, e:
            if isinstance(e.reason, socket.timeout):
	        raise MyException("There was an error : %r" %e)
	    else:
	        raise
                s=f.read()
                f.close()
                print s
                return s
    else:
	print "请输入正确的url"
getPage(url="http://www.zhanghui.com/")	


def max0f(*args):
	aSet=set()
	for lst in args:
		assert isinstance(lst,list),'Premeter is list only'
		aSet.update(lst)
	return max(aSet)
max0f(args=[1,2,3,4,5,6]);



def printinfo(name , age):
	print "Name:", name;
	print "Age:", age;
	return;
	
printinfo (age=50,name="zhanghui")




def printinfo(name,age = 35):
	print "Name: ", name;
	print "Age: ", age;
	return;

printinfo (age=50,name="zhanghui");
printinfo (name="huihui");



def printinfo(arg1, *vartuple):
	print "输出： "
	print arg1
	for var in vartuple:
		print var
	return;

printinfo(10);
printinfo(70,60,10,100);



sum = lambda arg1, arg2: arg1 + arg2

print "Value of total : ", sum(10 ,20)
print "Value of total: ", sum (20,20)




def sum(arg1 , arg2):
	total = arg1 + arg2
	print "Inside the function: ", total
	return total;

total = sum (10 , 20);
print "Outside the function : ", total




total = 0 ; #This is global variables.
 
def sum(arg1 , arg2):
	total = arg1 + arg2 ; 
	print "Inside the function local total: ", total
	return total;

sum( 10 ,20)
print "Outside the function global total", total
"""































"""
def printme( str ):
    print str;
    return;

printme( str = "My String");
"""











"""
def addOn(**arg):
    sum = 0
    if len(arg) == 0: return 0
    else:
        for x in arg.itervalues():
             sum += x
    return sum
addOn(x=4,y=5,k=6)
"""
