from django.shortcuts import render,HttpResponse
from myWebpage.models import feedback as Fb
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        'context':"Aditya sharma"
    }
    return render(request,'base.html',context)

def home(request):
    context = {
        'context':"Home"
    }
    return render(request,'home.html',context)
def Myprojects(request):
    context = {
        'context':"My Projects"
    }
    return render(request,'Myprojects.html',context)

def Feedback(request):
    context = { 'context':"feedback"   }
    if request.method == "POST":
        email = request.POST.get('email')
        feed = request.POST.get('feedback')
        date = datetime.today()
        f = Fb(email=email,feed=feed,date=date)
        f.save()
    return render(request,'feedback.html',context)

def blogs(request):
    context = {
        'context':"My Blogs"
    }
    return render(request,'blogs.html', context)
def b1(request):
    context = {
        'context':"blog 1"
    }
    return render(request,'blogstemp/b1.html',context)