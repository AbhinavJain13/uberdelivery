from django.shortcuts import render, redirect
from .models import Vendor, Menu
from .models import Restaurant
from ..userapp.models import Address
from django.contrib import messages
import usaddress

def index(request):
    return render(request, "vendorapp/index.html")

def next(request):
    info={
    'f_name':request.POST['f_name'],
    'l_name':request.POST['l_name'],
    'email':request.POST['email'],
    'addr':request.POST['addr'],
    'apt': request.POST['apt'],
    'city':request.POST['city'],
    'state':request.POST['state'],
    'zipcode': request.POST['zipcode'],
    'password':request.POST['password'],
    'cpassword':request.POST['cpassword'],
    'phone':request.POST['phone'],
    }

    context = {
    'basic':info
    }
    result = Vendor.objects.reg_valid(request.POST)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect('vendor:index')

    # address = Address.objects.create()

    request.session['vid']= result[1].id

    return render(request, "vendorapp/rest_details.html", context)


def print_messages(request, message_list):
    for message in message_list:
        print message
        messages.add_message(request, messages.INFO, message)

def register(request):
    result = Restaurant.objects.reg_valid(request.POST)

    if result[0] == False:
        print_messages(request, result[1])
        return render(request, "vendorapp/rest_details.html")
    thisvendor=Vendor.objects.get(id = request.session['vid'])
    thisvendor.rest.add(result[1])
    print result[1]

    print thisvendor.rest.all()

    return render(request, 'vendorapp/success.html')


def login(request):
    print request.method
    params = {
    'email': request.session['email'],
    'password':request.session['password'],
    }

    result = Vendor.objects.login_valid(params)
    if result[0] == False:
        print_messages(request, result[1])
        return redirect('main:index')
    request.session['id']=result[1].id
    for rest in result[1].rest.all():
        print rest.rest_name
    return login_success(request, result[1])

def addmenu(request):
    if request.method=='POST':
        thisvendor = Vendor.objects.get(id = request.session['id'])
        for rest in thisvendor.rest.all():
            print rest.rest_name
        # print thisvendor.rest.all
        thisrest = Restaurant.objects.get(id = request.POST['rest'])
        thismenu = Menu.objects.create(mon = request.POST['mon'], tues=request.POST['tues'], wed= request.POST['wed'], thurs= request.POST['thurs'], fri= request.POST['fri'], sat=request.POST['sat'], sun = request.POST['sun'], rest= thisrest)
        context = {
            'menu':thismenu
        }
        return render(request, 'vendorapp/dashboard.html', context)

def login_success(request, vendor):
    context = {
    'vendor' : Vendor.objects.get(id = request.session['id'])
    }
    return render(request, "vendorapp/dashboard.html", context)
