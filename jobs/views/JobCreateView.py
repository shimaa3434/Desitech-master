
from django.views.generic.edit import CreateView
from django.shortcuts import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.urls import reverse
from jobs.models import Job ,City
from jobs.forms.JobCreateForm import JobForm
from jobs.decorators import   is_company_or_admin
from django.contrib.auth.decorators import login_required

login_decorator = login_required (login_url = 'accounts:login')


@method_decorator(login_decorator, name='dispatch')
@method_decorator(is_company_or_admin, name='dispatch')

class JobCreateView(CreateView):
    login_required = True
    model = Job
    form_class = JobForm
    template_name = 'add_job.html'
   
    def get_success_url(self):
        return reverse('jobs:my-jobs')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.publish_By_id = self.request.user.id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

  
   