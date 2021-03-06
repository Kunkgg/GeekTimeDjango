import logging

from django.shortcuts import render

from jobs.models import Cities, Job, JobTypes

LOG = logging.getLogger()


def job_list(request):
    jobs = Job.objects.all()
    for job in jobs:
        job.job_type = JobTypes[job.job_type][1]
        job.job_city = Cities[job.job_city][1]
    context = {
        'jobs': jobs,
    }
    return render(request, 'jobs/job_list.html', context)


def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.job_type = JobTypes[job.job_type][1]
    job.job_city = Cities[job.job_city][1]
    context = {
        'job': job,
    }

    LOG.info(f"request method: {request.method}, path: {request.path}")
    return render(request, 'jobs/job_detail.html', context)
