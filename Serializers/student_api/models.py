from django.db import models

# Create your models here.
class Path(models.Model):
    path_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.path_name} "
    



class Student(models.Model):
    path= models.ForeignKey(Path, related_name='Student', on_delete=models.CASCADE)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.fname} "