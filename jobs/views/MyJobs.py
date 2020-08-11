from jobs.models import Job
from django.views import View
from django.contrib.auth.decorators import login_required
from jobs.decorators import is_company_or_admin
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.core.paginator import Paginator

login_decorator = login_required (login_url = 'accounts:login')

@method_decorator(login_decorator, name='dispatch')
@method_decorator (is_company_or_admin , name='dispatch' )

class MyJobs(View):

    def get (self , request):
        myjobs = Job.job_manger.filter (publish_By = request.user.id).order_by('-date')
        
        context =  {'myjobs' : myjobs , 'page_obj': myjobs}
        return render ( request , 'jobs_dashboard.html' , context )
   

