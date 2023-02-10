from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False,blank=False)
    roll = models.IntegerField(unique = True, null=False)
    emailid = models.EmailField(max_length=100, null=False)
    contactno = models.CharField(null=False,blank=False,unique=True,max_length=10)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    pincode = models.CharField(null=False,blank=False,max_length=7)


    def __str__(self):
        return self.name
