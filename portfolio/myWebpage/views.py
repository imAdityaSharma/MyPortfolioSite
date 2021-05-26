from django.shortcuts import render,HttpResponse

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