from django.shortcuts import render,redirect
from ..userapp .models import User,Address
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"mainapp/index.html")
def login(request):
    if request.method =="POST":
        if request.POST['member']=="vendor":
            return redirect('vendor:index')
        else:
            user=User.objects.login(request.POST)
            # print type(user)
            if 'error' in user:
                print user['error']
                context={
                    'errors':user['error']
                }
                return render(request,"mainapp/index.html",context)
            else:
                request.session['f_name']=user['user'].f_name
                request.session['userid']=user['user'].id
                return redirect("user:show")
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
