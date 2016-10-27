from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,"mainapp/index.html")

def login(request):
    if request.method =="POST":
        if request.POST['member']=="vendor":
            request.session['email'] = request.POST['email']
            request.session['password'] = request.POST['password']
            return redirect('vendor:login')
        else:
            return redirect('user:index')
    else:
        return redirect('main:index')

def register(request):
    if request.method =="POST":
        if request.POST['member']=="vendor":
            return redirect('vendor:index')
        else:
            return redirect('user:index')
    else:
        return redirect('main:index')
