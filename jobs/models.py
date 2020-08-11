from django.db import models
from accounts.models.User import User
from accounts.models.Country import Country
from accounts.models.City import City

# Create your models here.



class Job (models.Model):

    publish_By =models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=50) 
    skills = models.TextField()
    text = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    job_manger = models.Manager()


