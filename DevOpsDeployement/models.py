from django.db import models

# Create your models here.

class DevOpsStudents(models.Model):
    full_name = models.CharField(max_length=50)
    date = models.DateField()
    headline = models.CharField(max_length=200)
    fees = models.IntegerField(10)
    location = models.CharField(max_length=15)
    number = models.IntegerField(11)

    def __str__(self):
        return self.full_name

