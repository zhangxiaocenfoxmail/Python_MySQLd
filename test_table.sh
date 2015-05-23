#!/bin/bash

while true
     do
 mysql -utest -ptest -h192.168.21.219 -P3306 -Dgaodun -e "select count(*) from gd_paper_data_best_ds"
 mysql -utest -ptest -h192.168.21.219 -P3306 -Dgaodun -e "select count(*) from gd_paper_data_best_item"
 mysql -utest -ptest -h192.168.21.219 -P3306 -Dgaodun -e "select count(*) from gd_paper_data_best" 
done
