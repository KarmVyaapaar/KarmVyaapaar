from django.db import models

# Create your models here.
class Workers(models.Model):
    Worker_id = models.AutoField
    name = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=70,default="")
    Phone = models.IntegerField(default=0)
    email = models.CharField(max_length=50,default="")
    skills = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=50,default="")
    date = models.DateField()
    Image = models.ImageField(upload_to="images",default="")

    def __str__(self):
        return self.name

class Employer(models.Model):
    username = models.CharField(max_length=50,default="")
    firstname = models.CharField(max_length=50,default="")
    lastname = models.CharField(max_length=50,default="")
    phone = models.IntegerField(default=0)
    email = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.username
