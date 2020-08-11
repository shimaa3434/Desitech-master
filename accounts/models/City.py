from django.db import models
from accounts.models.Country import Country

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name