from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models.User import User 
from accounts.models.CompanyProfile import Company_profile
from accounts.models.JobSeekerProfile import job_seeker_profile
from accounts.models.Country import Country
from accounts.models.City import City
from django.contrib.auth.models import Group



class Company(admin.StackedInline):
    model = Company_profile
    can_delete = False
    verbose_name_plural = 'Company Profile'
    fk_name = 'user'

class JobSeeker(admin.StackedInline):
    model =  job_seeker_profile
    can_delete = False
    verbose_name_plural = 'Job Seeker Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):

    def Name (self , user ):
        profile = user.getProfile()
       
        if profile is None:
            return 'Admin'
        else:
            return profile.Name
     
    ordering = ('email',)
    list_display = ('Name' , 'user_type' , 'email' )
    list_display_links = ('Name' , 'email' )
    list_filter =  ('user_type' , 'is_staff' , 'is_active' ,)
    list_select_related = ['job_seeker_profile' , 'company_profile']
    search_fields = ('email', 'job_seeker_profile__Name' , 'company_profile__Name' ,)
    fieldsets = (
        (None,
                {'fields': ('email', 'password' ,'is_superuser' , 'is_staff' , 'is_active' , 'user_type' )}),
        )

    add_fieldsets = (
        (None, 
                {'fields': ('email', 'password1', 'password2' , 'user_type' , 'is_superuser' , 'is_staff' , 'is_active'),}),
        )



    def get_inline_instances(self, request, obj=None):
       
        if not obj:
            return list()
        if obj.is_superuser:
            self.inlines = ()
        if obj.user_type == 1:
            self.inlines =(Company ,)
        if obj.user_type == 2:
             self.inlines =(JobSeeker ,)
      
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register (City )
admin.site.register (Country )

admin.site.site_header = 'Desitech'
admin.site.site_title = 'Desitech'
admin.site.index_title = 'Admin'





