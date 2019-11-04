from django.shortcuts import render, get_object_or_404

#import the models so you can use the data stored in this table/model
from .models import Blog

# Create your views here.
def allblogs(request):
    #return all blogs
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

# Create your views here.
def detail(request, blog_id):
    # blog_id was passed in from
    # 1) the url from template allblogs.html: <a href="{% url 'detail' blog.id %}">
    # 2) the blog_id value specified in the URL pattern in blog/urls.py: path('<int:id>/', views.detail, name='detail')
    id = blog_id

    #get specific blog using the id passed.
    #blog = Blog.objects.get(pk=id)
    # ALTHOUGH IT IS BETTER TO RETURN A 404 IF NOT FOUND, make sure to import it
    blog = get_object_or_404(Blog, pk=id)


    return render(request, 'blog/detail.html', {'blog':blog})
