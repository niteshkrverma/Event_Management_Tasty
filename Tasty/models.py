from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name
class Booking(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    f_name=models.CharField(max_length=200)
    date =models.DateField(auto_now=False, auto_now_add=False)
    number=models.BigIntegerField(blank=False)
    status = models.CharField(max_length=100,default='Pending')
    venue=models.CharField(max_length=100,blank=True)
    day=models.IntegerField(blank=True)
    guest=models.IntegerField(blank=True)
   

    def __str__(self):
        return self.user.username