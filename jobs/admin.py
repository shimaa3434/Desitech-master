from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from jobs.models import Job 
from jobs.forms.JobCreateForm import JobForm

# Register your models here.



class CustomJobAdmin(admin.ModelAdmin):
   
    def Name (self , job ):
        profile = job.publish_By.getProfile()
        if profile is None:
            return 'Admin'
        else:
            return profile.Name
      
    form = JobForm
    ordering = ('date',)
    list_display = ('title' , 'Name' , 'country' , 'city' ,'date' ,)
    list_display_links = ('title' , 'country' , 'city' )
    list_filter =  ('title' , 'country' , )
    search_fields = ('title' , 'publish_By__email' ,)

admin.site.register (Job , CustomJobAdmin )

 
