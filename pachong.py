#!/usr/bin/env python
# encoding: utf-8

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@file: pachong.py
@time: 2016-09-11 10:29
"""

import requests,pymysql,re
conn = pymysql.connect(host='mysql.litianqiang.com', port=7150,user='xiaoshuo',passwd='qiangzi()',db='xiaoshuo',charset='UTF8')

ret = requests.get('http://game.litianqiang.com/')

data=re.findall('''<li><a href="(\d+)"><span class="new"></span><img alt="(.*?)" src="(.*?)" />.*?</a></li>''',ret.text)
for i in data:
    print(i)
    cur = conn.cursor()
    sql='''insert into youxiapp_youxi (name,imgurl,flashurl) values('{}','{}','{}')'''.format(i[1],i[2],'http://game.litianqiang.com/{}'.format(i[0]))
    cur.execute(sql)

conn.commit()
cur.close()
conn.close()