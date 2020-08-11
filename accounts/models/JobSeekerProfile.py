from django.db import models
from accounts.models.User import User
from django.core.validators import FileExtensionValidator
from accounts.models.Country import Country
from accounts.models.City import City
from django.conf import settings
from django.core.validators import RegexValidator



class job_seeker_profile (models.Model):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , primary_key=True)
    Name = models.CharField(max_length=30 , null=False)
    surname = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    country_of_residence = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    zip_code =  models.CharField("ZIP / Postal code", max_length=12,)
    street =models.CharField(max_length=128)
    house_number = models.IntegerField(null=True)
    personal_photo =models.ImageField(upload_to='images/')
    CV = models.FileField(upload_to='CV/',validators=[FileExtensionValidator(allowed_extensions=['pdf'])]) 
    cover_letter = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) 


