from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200) 

class Contact(models.Model):
    emailid=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    message=models.CharField(max_length=500)
    
    def __str__(self):
        return self.emailid +""+ self.mobile+ ""+ self.message