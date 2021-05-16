from django.db import models

from datetime import date


class Advisor(models.Model):
    advisor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    grade = models.CharField(max_length=3, blank=True, null=True)
    room_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'advisor'



class Parent(models.Model):
    parent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'parent'


class Student(models.Model):

    def default_dict():
       return {'0' : 0, '1': 0, '2': 0, '3': 0, '4': 0}

    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    parent = models.ForeignKey(Parent, models.CASCADE, blank=True, null=True)
    advisor = models.ForeignKey(Advisor, models.CASCADE, blank=True, null=True)
    grade = models.CharField(max_length=4, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    activity_curr = models.JSONField(default=default_dict, blank=True, null=True)
    activity_base = models.JSONField(default=default_dict, blank=True, null=True)
    route_no = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        db_table = 'student'


class ActivityDetail(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(blank=True, null=True, max_length=100)
    detail = models.CharField(blank=True, null=True, max_length=255)


class UpdateRequest(models.Model):
    student = models.IntegerField(blank=False, null=False)
    activityDetail = models.ForeignKey(ActivityDetail, models.CASCADE)
    permanent = models.BooleanField(default=False)
    start_date = models.DateField(default=date.today())


class ActivityChange(models.Model):
    student = models.ForeignKey(Student, models.CASCADE)
    start_date = models.DateField()
    activity_type = models.ForeignKey(ActivityDetail, models.CASCADE)
    permanent = models.BooleanField(default=False)
