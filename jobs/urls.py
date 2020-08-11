from django.urls import path 
from jobs.views import (JobCreateView , JobDeleteView , JobDetailView , 
                        JobUpdateView , AllJobsView , JobSearchView , MyJobs ,views)



app_name = 'jobs'

urlpatterns = [
 
    path('listjobs/', AllJobsView.AllJobsView.as_view(), name='all-jobs-list'),
    path('myjobs/', MyJobs.MyJobs.as_view(),name='my-jobs'),
    path('create/', JobCreateView.JobCreateView.as_view(), name='job-create'),
    path('<int:pk>/', JobDetailView.JobDetailView.as_view(),name='job-detail'),
    path('<int:pk>/update',JobUpdateView.JobUpdateView.as_view(),name='job-update'),
    path('<int:pk>/delete', JobDeleteView.JobDeleteView.as_view(),name='job-delete'),
    path('search/', JobSearchView.JobSearch.as_view(),name='job-search'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities')
]
