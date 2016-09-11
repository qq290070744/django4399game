from django.shortcuts import render
import os,pymysql
conn = pymysql.connect(host='mysql.litianqiang.com', port=7150,user='xiaoshuo',passwd='qiangzi()',db='xiaoshuo',charset='UTF8')
cur = conn.cursor()
cur.execute("select * from youxiapp_youxi")

os.environ['DJANGO_SETTINGS_MODULE']='game.settings'
import django
django.setup()
from youxiapp import models
# Create your views here.
obj=models.youxi.objects.all()
for i in obj:
    print(i)
def youxi(request):
    return render(request,'index.html',{'xy':obj})