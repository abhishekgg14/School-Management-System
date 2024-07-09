from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    type=models.CharField(max_length=10)

class dept_table(models.Model):
    dept_name=models.CharField(max_length=50)

class course_table(models.Model):
    course_name=models.CharField(max_length=50)
    DEPT=models.ForeignKey(dept_table,on_delete=models.CASCADE)

class sub_table(models.Model):
    sub_name=models.CharField(max_length=50)
    COURSE=models.ForeignKey(course_table,on_delete=models.CASCADE)
    sem=models.BigIntegerField()

class staff_table(models.Model):
    stf_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    DEPT=models.ForeignKey(dept_table,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    img=models.FileField()

class stud_table(models.Model):
    std_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    place=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    COURSE=models.ForeignKey(course_table,on_delete=models.CASCADE)
    sem=models.BigIntegerField()
    img=models.FileField()

class notes_table(models.Model):
    title=models.CharField(max_length=100)
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    SUB=models.ForeignKey(sub_table,on_delete=models.CASCADE)
    file=models.FileField()

class assign_table(models.Model):
    STAFF=models.ForeignKey(staff_table,on_delete=models.CASCADE)
    SUB=models.ForeignKey(sub_table,on_delete=models.CASCADE)

