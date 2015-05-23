#!/bin/bash
mysql -uroot -ppassword -h192.168.21.214 -P3307 gaodun4  -e "delete from gd_paper_wrong"
mysql -uroot -ppassword -h192.168.21.214 -P3307 gaodun5  -e  "delete from gd_paper_wrong"
mysql -uroot -ppassword -h192.168.21.214 -P3307 gaodun6  -e "delete from gd_paper_wrong"


mysql -uroot -ppassword -h192.168.21.219 -P3307 gaodun1  -e "delete from gd_paper_wrong"
mysql -uroot -ppassword -h192.168.21.219 -P3307 gaodun2  -e  "delete from gd_paper_wrong"
mysql -uroot -ppassword -h192.168.21.219 -P3307 gaodun3  -e "delete from gd_paper_wrong"
