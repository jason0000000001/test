from unicodedata import name
from django.db import models
import django.utils.timezone as timezone

# Create your models here.
'''
class Room(models.Model):
    image_id = models.IntegerField(db_column='imageid', default = 0)
    name = models.CharField(max_length=45)
    #description = models.TextField(blank=True, null=True)
    birthday = models.CharField(max_length=45, default = "2002/07/11")
    sex = models.CharField(max_length=45, default = "male")
    temperature = models.FloatField(default = 0)
    weight = models.FloatField(default = 0)
    height = models.FloatField(default = 0)
    pressures = models.IntegerField(db_column='pressureS', default = 0)
    pressured = models.IntegerField(db_column='pressureD', default = 0)
    #updated = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
'''

class User(models.Model):
    image_id = models.IntegerField(db_column='imageid')#圖片id
    name = models.CharField(max_length=45)#姓名
    birthday = models.CharField(max_length=45, default = "2000/01/01")#出生年月日
    sex = models.CharField(max_length=45, default = "male")#性別
    height = models.FloatField(default = 0.0)#身高
    createtime = models.DateTimeField(auto_now_add = timezone.now)#創建時間
    #updatetime = models.DateTimeField(auto_now = True)#更新時間


    def __str__(self):
        return self.name


class Data(models.Model):
    #name = models.CharField(max_length=45)
    userid = models.ForeignKey(User, on_delete=models.CASCADE,default = False)#使用者id 
    temperature = models.FloatField(default = 0.0)#體溫
    weight = models.FloatField(default = 0.0)#體重
    pressures = models.IntegerField(db_column='pressureS', default = 0)#收縮壓
    pressured = models.IntegerField(db_column='pressureD', default = 0)#舒張壓
    heartbeat = models.IntegerField(default=0)#心跳
    bmi = models.FloatField(default = 0.0)#bmi
    bmr = models.FloatField(default = 0.0)#bmr
    result1 = models.CharField(max_length=100,default = True)#血壓建議
    result2 = models.CharField(max_length=100,default = True)#體溫建議
    result3 = models.CharField(max_length=100,default = True)#bmi建議
    result4 = models.CharField(max_length=100,default = True)#心跳建議
    createtime = models.DateTimeField(auto_now_add = timezone.now)#創建時間
    #updatetime = models.DateTimeField(auto_now = True)#更新時間


    #def __str__(self):
    #    return self.name


class Medicine(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE,default = False)#使用者id 
    medicine = models.TextField(null=True)


    def __str__(self):
        return self.medicine