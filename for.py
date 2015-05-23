#!/usr/bin/env python
import time, MySQLdb
import re
import os
import sys
reload(sys)
sys.setdefaultencoding( "utf8" )
a=0
b=200000
for i in range(1,12):
    a+=200000
    b+=200000
    print (a)
    print (b)
