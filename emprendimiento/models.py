from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Day(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'day'


class Emprendimiento(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    type = models.CharField(max_length=50)
    join_date = models.DateTimeField()
    image_url = models.CharField(max_length=250, blank=True, null=True)
    telephones = models.JSONField(blank=True, null=True)
    categories = models.JSONField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'emprendimiento'


class Review(models.Model):
    emprendimiento = models.ForeignKey(Emprendimiento, models.DO_NOTHING)
    username = models.CharField(max_length=100)
    score = models.IntegerField()
    comment = models.CharField(max_length=250, blank=True, null=True)
    images_url = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Schedule(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    emprendimiento = models.ForeignKey(Emprendimiento, models.DO_NOTHING)
    day = models.ForeignKey(Day, models.DO_NOTHING)
    opening_hour = models.TimeField()
    closing_hour = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule'


class User(models.Model):
    user_id = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateTimeField()
    join_date = models.DateTimeField()
    role = models.CharField(max_length=20)
    authorities = models.JSONField(blank=True, null=True)
    profile_image_url = models.CharField(max_length=250, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    last_login_date_display = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_not_loked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

