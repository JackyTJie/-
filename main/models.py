from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    checkcode = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    clas = models.IntegerField()
    level = models.IntegerField()
    BBcoin = models.IntegerField()
    star = models.CharField(max_length=1000)


class Info(models.Model):
    id = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=400)
    picture = models.CharField(max_length=300)
    gift = models.CharField(max_length=300)
    fromu = models.CharField(max_length=50)
    hide = models.CharField(max_length=5)


class Com(models.Model):
    id = models.IntegerField(primary_key=True)
    idstr = models.CharField(max_length=10)
    tarInfo = models.IntegerField()
    text = models.CharField(max_length=100)
    picture = models.CharField(max_length=300)
    thumb = models.IntegerField()
    fromu = models.CharField(max_length=50)

