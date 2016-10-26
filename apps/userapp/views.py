from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"userapp/index.html")
def register(request):
    valid=User.objects.validate(request.POST)
    return redirect('main:index')
