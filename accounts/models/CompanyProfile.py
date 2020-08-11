from django.db import models
from accounts.models.User import User
from accounts.models.Country import Country
from accounts.models.City import City
from django.conf import settings
from django.core.validators import RegexValidator

class Company_profile (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , primary_key=True)
    Name =models.CharField(max_length=50 )
    country = models.ForeignKey(Country, on_delete=models.SET_NULL , null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL , null=True)
    street = models.CharField(max_length=128)
    building_number = models.IntegerField()
    zip_code =  models.CharField("ZIP / Postal code", max_length=12,)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) 
    mobile_number = models.CharField(validators=[phone_regex], max_length=17) 
   