from django.db import models
from django.contrib.auth.models import AbstractBaseUser  , PermissionsMixin
from accounts import models as mo
from accounts.models.UserManger import UserManager

class User (AbstractBaseUser , PermissionsMixin):

    email = models.EmailField(unique=True , null=False)


    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
  
    ADMIN = 0
    COMPANY = 1
    JOB_SEEKER = 2
    
    REQUIRED_FIELDS = ['user_type']
    USERNAME_FIELD = 'email' 

    _TYPE = ((ADMIN , 'admin') , (COMPANY , 'company') , (JOB_SEEKER , 'job_seeker') )
    user_type  = models.PositiveSmallIntegerField (choices=_TYPE  )


    def is_company (self):
      
        if self.user_type == 1:
            return True
        return False

    def is_job_seeker (self) :
        if self.user_type == 2:
            return True
        return False

    def getProfile (self):
        if self.user_type == 1:
            profile = mo.CompanyProfile.Company_profile.objects.get (user = self)
            return profile
        elif self.user_type == 2 :
            profile = mo.JobSeekerProfile.job_seeker_profile.objects.get (user = self)
            return  profile
    
    objects = UserManager ()