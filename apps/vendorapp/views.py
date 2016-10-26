from django.shortcuts import render, redirect
from .models import Vendor
from .models import Restaurant
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
    return render(request, 'vendorapp/dashboard.html')

def login(request):
    result = Vendor.objects.login_valid(request.POST)
