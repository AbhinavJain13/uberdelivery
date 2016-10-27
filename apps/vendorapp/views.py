from django.shortcuts import render, redirect
from .models import Vendor
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

    newaddress = usaddress.tag(request.POST['addr']+","+request.POST['apt']+","+ request.POST['city']+","+request.POST['state']+","+request.POST['zipcode'])
    print "done"

    address = Address.objects.create(addressNumber=newaddress[0].get('AddressNumber',''), addressNumberPrefix=newaddress[0].get('AddressNumberPrefix',''), addressNumberSuffix=newaddress[0].get('AddressNumberSuffix',''), buildingName=newaddress[0].get('BuildingName',''), occupancyType=newaddress[0].get('OccupancyType',''), occupancyIdentifier=newaddress[0].get('OccupancyIdentifier',''), placeName=newaddress[0].get('PlaceName',''),
    stateName=newaddress[0].get('StateName',''), streetName=newaddress[0].get('StreetName',''), streetNamePreDirectional=newaddress[0].get('StreetNamePreDirectional',''), streetNamePreType=newaddress[0].get('StreetNamePreType',''), streetNamePostDirectional=newaddress[0].get('streetNamePostDirectional',''), streetNamePostType= newaddress[0].get('StreetNamePostType',''),subaddressType=newaddress[0].get('SubaddressType',''), uSPSBoxType=newaddress[0].get('USPSBoxType',''), zipCode=newaddress[0].get('ZipCode',''))
    # address = Address.objects.create()


    print vars(address)
    print address.addressNumber
    print address.placeName
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
    return login_success(request, result[1])

def login_success(request, vendor):
    request.session['vendor'] = {
        'id' : vendor.id,
        'f_name' : vendor.f_name,
        'email' : vendor.email,
    }
    return render(request, "vendorapp/dashboard.html")
