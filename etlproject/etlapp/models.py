from django.db import models

# Source table (raw data)
class StudentRaw(models.Model):
    student_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    course = models.CharField(max_length=50, null=True)

# Target table (cleaned data)
class StudentClean(models.Model):
    student_id = models.IntegerField()
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)



