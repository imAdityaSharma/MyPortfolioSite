from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'context':"Aditya sharma"
    }
    
    return render(request,'base.html',context)
