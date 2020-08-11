from django.core.exceptions import PermissionDenied
from functools import wraps

from jobs.models import Job



def company_is_publish_job(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        _job = Job.job_manger.get(pk=kwargs['pk'])
        if _job.publish_By_id == request.user.id:
             return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
  return wrap

def is_admin(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 0:
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_company(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 1  :
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_job_seeker(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 2:
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

def is_company_or_admin(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        if  request.user.user_type == 0 or request.user.user_type == 1 :
             return function(request, *args, **kwargs)
        else:
             raise PermissionDenied
  return wrap

