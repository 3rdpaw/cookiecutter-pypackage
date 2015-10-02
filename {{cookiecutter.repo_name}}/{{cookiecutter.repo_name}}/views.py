"""
views.py
@author: mbutt

"""
import collections
import traceback

from django.conf import settings

from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from celery.result import AsyncResult

from adapters.{{cookiecutter.repo_name}} import tasks

from feed.models import Feed
from models import *
from crashlog import models as crashlog


CELERY_DONE_STATES = ['SUCCESS', 'FAILURE', 'REVOKED']
MAX_JOB_HISTORY = 5

JobStatus = collections.namedtuple('JobStatus', 'task_id state output_file')


@login_required
def process_settings(request):
    request.breadcrumbs([("Adapter - Settings", ""), ])
    cfg = query_user_settings(request.user)
    cfg.save()
    return redirect(reverse('{{cookiecutter.repo_name}}_process'))
    # return render(request, 'snort_adapter-settings.html', {'settings': cfg})
    # return my_settings


def query_user_settings(user):
    # Query mongo for existing settings for the user_id, otherwise default
    try:
        cfg = SnortAdapterConf.objects.get(user_id=user.id)
    except:
        # build default settings for user_id and save
        cfg = {{cookiecutter.repo_name}}AdapterConf()
        cfg.set_defaults(user)
    return cfg


def update_user_jobs(user):
    """
    Update the status via celery for any jobs this user has
    :param user:
    :return:
    """
    try:
        jobs = JobInfo.objects(created_by=user.id, job_active=True)
        if jobs:
            for job in jobs:
                # update job status for this user's active jobs
                result = AsyncResult(job.task_id)
                if result.state in CELERY_DONE_STATES:
                    job.job_active = False
                    job.job_state = result.state
                    job.save()
                if job.job_state != result.state:
                    job.job_state = result.state
                    job.save()
    except Exception as e:
        crashlog.save('{{cookiecutter.repo_name}}', str(e), traceback.format_exc())


def query_user_jobs(user):
    """

    :param user:
    :return:
    """
    jobs = {}
    try:
        jobs = JobInfo.objects(created_by=user.id).order_by('-job_start')[:MAX_JOB_HISTORY]
    except Exception as e:
        crashlog.save('{{cookiecutter.repo_name}}', str(e), traceback.format_exc())
    return jobs


def build_settings(request):
    request.breadcrumbs([("Adapter - Settings", ""), ])

    # get settings from db
    settings = query_user_settings(request.user)
    return render(request, '{{cookiecutter.repo_name}}-settings.html', {'settings': settings})


@login_required
def settings(request, internal_link=False):
    if internal_link:
        return build_settings(request)
    if request.method == 'POST':
        return process_settings(request)
    else:
        return build_settings(request)


def get_joblist(request):
    user_jobs = query_user_jobs(request.user)
    joblist = [JobStatus(task_id=job.task_id, state=job.job_state, output_file=job.output_file) for job in user_jobs]
    return joblist

