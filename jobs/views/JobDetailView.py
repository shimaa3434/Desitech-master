from django.views.generic.detail import DetailView
from jobs.models import Job


class JobDetailView(DetailView):

    model = Job
    template_name = 'job_detail.html'
    context_object_name = 'job'
