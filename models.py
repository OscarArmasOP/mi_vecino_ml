# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Day(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'day'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    giro = models.CharField(max_length=100, blank=True, null=True)

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
    liked = models.CharField(max_length=500, blank=True, null=True)
    likedd = models.JSONField(blank=True, null=True)
    likeddd = models.JSONField(blank=True, null=True)
    favorite_emprendimientos = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class User2(models.Model):
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
    liked = models.CharField(max_length=500, blank=True, null=True)
    likedd = models.JSONField(blank=True, null=True)
    favorite_emprendimientos = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user2'
