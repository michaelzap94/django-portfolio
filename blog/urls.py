from django.urls import path
from . import views
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('detail/<int:id>/', views.allblogs, name='detail')
]