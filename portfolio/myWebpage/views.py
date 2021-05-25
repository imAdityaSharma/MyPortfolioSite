from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'context':"Aditya sharma"
    }
    
    return render(request,'base.html',context)
def blogs(request):
    return render(request,'blogs.html')
def b1(request):
    return render(request,'b1.html')