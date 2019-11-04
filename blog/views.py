from django.shortcuts import render

#import the models so you can use the data stored in this table/model
from .models import Blog

# Create your views here.
def allblogs(request):
    #return all blogs
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
