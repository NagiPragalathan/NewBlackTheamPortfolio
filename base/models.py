from django.db import models
import uuid

class skill(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    language = models.CharField(max_length=50)
    persentage = models.IntegerField()


class resume(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=50)
    last_date = models.CharField(max_length=50)


class atchviements(models.Model):
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)


class certificate(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)


class projects(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=500)
    topic = models.CharField(max_length=500)
    date_place = models.CharField(max_length=500)
    paragraph = models.CharField(max_length=500)
    

class hackthons(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    sub_topic = models.CharField(max_length=50)
    date_place = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    result = models.CharField(max_length=50)


class Roles(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    discrption = models.CharField(max_length=50)
    link = models.CharField(max_length=50)


class profile_pic(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    img = models.CharField(max_length=100)

