from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_name = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=15)
    phone_ext = models.CharField(max_length=10, blank="True")
    email = models.EmailField()
    comments = models.TextField()
    company_name = models.CharField(max_length=250)

 
