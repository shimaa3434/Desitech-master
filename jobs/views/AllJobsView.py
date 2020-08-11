from django.views.generic import ListView
from jobs.models import Job

class AllJobsView(ListView):

    model = Job
    template_name = 'list_jobs.html'
    context_object_name = 'jobs'
    paginate_by =10
    ordering = ['date']
    jobs = Job.job_manger.all()

    def get_context_data(self, **kwargs):
        context = super(AllJobsView, self).get_context_data(**kwargs)
        
        jobs = self.get_queryset()
        context['jobs'] = jobs

       

        return context