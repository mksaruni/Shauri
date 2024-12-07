rom django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
       return self.name
