from django.db import models

# Create your models here.
class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.fname} {self.lname}"