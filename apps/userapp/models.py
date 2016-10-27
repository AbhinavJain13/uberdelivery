from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def validate(self,param):
        errors=[]
        user=User.objects.filter(email=param['email'])
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(param['f_name'])<1 and len(param['f_name'])<3:
            errors.append("firstname cannot be blank or less then 3")
        if len(param['l_name'])<1 and len(param[l_name])<3:
            errors.append("lastname cannot be blank or less than 3")
        if not EMAIL_REGEX.match(user['email']) and len(param['email'])<1:
            errors.append("invalid email or email cannot be blank")
        if len(param['addr'])<1:
            errors.append("address cannot be blank")

        if len(param['city'])<1:
            errors.append("city cannot be blank")
        if len(param['state'])<1:
            errors.append("state cannot be blank")
        if len(param['zipcode'])<5:
            errors.append("zipcode cannot be blank")
        if len(param['phone'])<10:
            errors.append("phone cannot be blank or less than 10 digits")
        if len(param['password'])<1:
            errors.append("password cannot be blank")
        if param['cpassword'] == param['password']:
            errors.append("password and confirm password do not match")
        if user>0:
            errors.append("email already exist")
        if len(errrors)>0:
            return(False,errors)
        else:
            address = Address.objects.create(addressNumber=newaddress[0].get('AddressNumber',''), addressNumberPrefix=newaddress[0].get('AddressNumberPrefix',''), addressNumberSuffix=newaddress[0].get('AddressNumberSuffix',''), buildingName=newaddress[0].get('BuildingName',''), occupancyType=newaddress[0].get('OccupancyType',''), occupancyIdentifier=newaddress[0].get('OccupancyIdentifier',''), placeName=newaddress[0].get('PlaceName',''),
            stateName=newaddress[0].get('StateName',''), streetName=newaddress[0].get('StreetName',''), streetNamePreDirectional=newaddress[0].get('StreetNamePreDirectional',''), streetNamePreType=newaddress[0].get('StreetNamePreType',''), streetNamePostDirectional=newaddress[0].get('streetNamePostDirectional',''), streetNamePostType= newaddress[0].get('StreetNamePostType',''),subaddressType=newaddress[0].get('SubaddressType',''), uSPSBoxType=newaddress[0].get('USPSBoxType',''), zipCode=newaddress[0].get('ZipCode',''))
            self.create(f_name=param['f_name'],l_name=param['l_name'],email=param['email'],)
            return(True,True)

class Address(models.Model):
    addressNumber=models.CharField(max_length=10)
    addressNumberPrefix=models.CharField(max_length=20)
    addressNumberSuffix=models.CharField(max_length=20)
    buildingName=models.CharField(max_length=10)
    occupancyType=models.CharField(max_length=20)
    occupancyIdentifier=models.CharField(max_length=20)
    placeName=models.CharField(max_length=20)
    stateName=models.CharField(max_length=20)
    streetName=models.CharField(max_length=20)
    streetNamePreDirectional=models.CharField(max_length=20)
    streetNamePreType=models.CharField(max_length=20)
    streetNamePostDirectional=models.CharField(max_length=20)
    streetNamePostType=models.CharField(max_length=20)
    subaddressType=models.CharField(max_length=20)
    uSPSBoxType=models.CharField(max_length=20)
    zipCode=models.CharField(max_length=5)

class User(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    address=models.ManyToManyField(Address,related_name="useraddress")
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=255)

    objects=UserManager()
