#!/bin/env python

import re
import os
import pymongo
connection=pymongo.Connection(host='192.168.0.16',port=27017)
db = connection.jrd
collection = db.system_log
#print collection.find({"user_reserve" : [ ]})

cursor = collection.find({},{"user_id": 1,"ctime":1})
for i in cursor :
 print i
