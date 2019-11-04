from django.shortcuts import render

#GET THE JOB model, so you can access the JOB table db
from .models import Job

# Create your views here.
def home(request):
    #retrieve all jobs, in objects form
    jobs = Job.objects
    print(jobs)
    print(jobs.all)
    print(type(jobs))
    return render(request, 'jobs/home.html', {'jobs':jobs})
