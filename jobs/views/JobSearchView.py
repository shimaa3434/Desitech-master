from django.views.generic import ListView
from jobs.models import Job
from django.views import View
from django.shortcuts import HttpResponse ,render 
from django.views.generic import ListView

class JobSearch (ListView):
    model = Job
    template_name = 'list_jobs.html'
    context_object_name = 'jobs'
   
    ordering = ['date']
    
    def get_queryset (self ):
        city = self.request.GET.get('city')
       
        jobsWithSlug = job.job_manger.filter (city =city)
        return jobsWithSlug

    def get_context_data(self, **kwargs):
        context = super(JobSearch, self).get_context_data(**kwargs)
        
        jobs = self.get_queryset()
        context['page_obj'] = jobs

        return context
