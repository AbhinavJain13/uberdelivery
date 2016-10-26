from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"mainapp/index.html")
def login(request):
    return render(request,"userapp/userdashboard.html")
def register(request):
    if request.method =="POST":
        if request.POST['member']=="vendor":
            return redirect('vendor:index')
        else:
            return redirect('user:index')
    else:
        return redirect('main:index')
