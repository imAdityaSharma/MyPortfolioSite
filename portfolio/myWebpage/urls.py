from django.contrib import admin
from django.urls import path,include
from myWebpage import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name="home"),
    path('blogs',views.blogs,name="blogs")
]
