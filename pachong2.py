#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: pachong2.py
@time: 2016-09-11 12:52
"""
import requests,re,pymysql
conn = pymysql.connect(host='mysql.litianqiang.com', port=7150,user='xiaoshuo',passwd='qiangzi()',db='xiaoshuo',charset='UTF8')
num=1
flashurl=[]
while True:
    ret = requests.get('http://game.litianqiang.com/{}'.format(num))
    url=re.findall('''src="(.*?)"''',ret.text)
    print(url[0])
    cur = conn.cursor()
    sql = '''update youxiapp_youxi set flashurl='{}' where id={} '''.format(url[0],num)
    cur.execute(sql)

    num+=1
    if num>=230:
        break
conn.commit()
cur.close()
conn.close()