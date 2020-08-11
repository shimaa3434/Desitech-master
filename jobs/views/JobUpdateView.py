from django.views.generic.edit import UpdateView
from jobs.models import Job
from django.urls import reverse
from jobs.decorators import  company_is_publish_job , is_company_or_admin 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from jobs.forms.JobCreateForm import JobForm

login_decorator = login_required (login_url = 'accounts:login')

@method_decorator(login_decorator, name='dispatch')
@method_decorator(company_is_publish_job, name='dispatch')
@method_decorator(is_company_or_admin, name='dispatch')

class JobUpdateView(UpdateView):

    model = Job
    form_class = JobForm
    template_name = 'update_job.html'
    context_object_name = 'job'
   

    def get_success_url(self):
        return reverse('jobs:my-jobs')

 
