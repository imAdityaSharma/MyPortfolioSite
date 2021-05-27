from django.contrib import admin
from django.urls import path,include
from myWebpage import  views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.index,name="home"),
    path('home',views.home,name="home"),
    path('myprojects',views.Myprojects,name="Myprojects"),
    path('blogs',views.blogs,name="blogs"),
    path('feedback',views.Feedback,name="feedback"),
    #blogs templates are stored in 'template/blogstemp/' directory new pages will be added here from now
    path('blogstemp/b1',views.b1,name="b1")
]
#openvpn --config adityam12123.first.ovpn