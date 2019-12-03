from django.shortcuts import render

#GET THE JOB model, so you can access the JOB table db
from .models import Job

# Create your views here.
def home(request):
    #retrieve all jobs, in objects form
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})
