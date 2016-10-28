from django.shortcuts import render,redirect
from .models import User,Address
from ..vendorapp.models import Restaurant
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"userapp/index.html")
def register(request):
    valid=User.objects.validate(request.POST)
    if valid[0]==False:
        print "false"
        print_messages(request, valid[1])
        return redirect('user:index')
    else:
        user=User.objects.get(id=valid[1].id)
        request.session['rid']=user.id
        print request.session['rid']
        print user
        return redirect('user:code')

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)
def code(request):
    if request.method=="POST":
        user1=User.objects.get(id=request.session['rid'])
        code_send= user1.code
        if code_send == request.POST['code']:
            context={
            'msg':"successful",

            }
            print "success"
            user1.valid=True
            user1.save()
            return render(request,"mainapp/index.html",context)
        else:
            print "unsuccessful"
            return render(request,"userapp/index.html")
    else:
        return render(request,"userapp/index.html")
# def login(request):
#     if request.method == "POST":
#         user=User.objects.login(request.POST)
#         # print type(user)
#         if 'error' in user:
#             print user['error']
#             context={
#                 'errors':user['error']
#             }
#             return render(request,"mainapp/index.html",context)
#         else:
#             request.session['name']=user['user'].name
#             request.session['userid']=user['user'].id
#         return redirect("user:show")

def show(request):
    context={
    'msg':"successful login",
    'users':User.objects.get(id=request.session['userid'])
    }
    return render(request,"userapp/userdashboard.html",context)
def filter_rest(request):
    if request.method=="POST":
        rests=Restaurant.objects.filter(services=request.POST['service']).filter(cuisine=request.POST['cuisine'])
        # for rest in rests.address.all():
        #     (rest.address.zipCode == request.POST['zip'])
        print vars(rests)
        context={
        'rest':rests,
        }
        return render(request,"userapp/userdashboard.html",context)
