from __future__ import unicode_literals
from django.db import models
import re, bcrypt
import usaddress

class VendorManager(models.Manager):
    def valid_inputs(self, vendor_info):

        EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        PHONE_REGEX=re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
        errors=[]

        if len(vendor_info['f_name']) < 3 or len(vendor_info['l_name']) < 3:
            errors.append("Names should be longer than 3 characters")

        if not re.match(EMAIL_REGEX, vendor_info['email']):
            errors.append("Enter a valid email format eg:abc@xyz.com")

        if len(vendor_info['addr']) < 3:
            errors.append("Address should be longer than 3 characters")

        if len(param['city'])<1:
            errors.append("city cannot be blank")

        if len(param['state'])<1:
            errors.append("state cannot be blank")

        if not re.match(PHONE_REGEX, vendor_info['phone']):
            errors.append("Enter a valid phone format eg:123 456 7890")

        if len(vendor_info['password']) < 1:
            errors.append("Password should be longer than 8 characters")

        if len(vendor_info['zipcode']) < 5:
            errors.append("Enter a 5 digit zipcode")

        if not str(vendor_info['password'])== str(vendor_info['cpassword']):
            errors.append("passwords do not match")

        return errors

    def reg_valid(self, vendor_info):
        errors = self.valid_inputs(vendor_info)
        if len(errors)>0:
            return(False, errors)
        else:
            pw_hash = bcrypt.hashpw(vendor_info['password'].encode(), bcrypt.gensalt())
            vendor = self.create(f_name = vendor_info['f_name'],l_name = vendor_info['l_name'], email = vendor_info['email'], password = pw_hash, cpassword = vendor_info['cpassword'], phone = vendor_info['phone'])

            print vendor.f_name

            return (True, vendor)

    def login_valid(self, params):
            vendor = Vendor.objects.filter(email=params['email'])
            if vendor:
                if bcrypt.hashpw(params['password'].encode(), vendor[0].password.encode()) == vendor[0].password.encode():
                    return (True, vendor[0])
                else:
                    return (False, ["Email/password do not exist"])
            else:
                return (False, ["Email/password do not exist"])



    def __str__(self):
            return self.id

class Vendor(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cpassword = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = VendorManager()


class RestaurantManager(models.Manager):
    def valid_inputs(self,rest_info):
        PHONE_REGEX=re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')
        errors=[]

        if len(rest_info['rest_name']) < 1:
           errors.append("Restaurant Name should be longer than 1 character")

        if len(rest_info['rest_addr']) < 3:
            errors.append("Address should be longer than 3 characters")

        if len(rest_info['phone']) < 10:
            errors.append("Enter your 10 digit Phone Number eg:123 456 7890")

        if not re.match(PHONE_REGEX, rest_info['phone']):
            errors.append("Not a valid phone format")

        return errors

    def reg_valid(self, rest_info):
        errors = self.valid_inputs(rest_info)
        if len(errors)>0:
            return(False, errors)
        else:
            rest = self.create(rest_name = rest_info['rest_name'], phone = rest_info['phone'], cuisine = rest_info['cuisine'], services = rest_info['services'], drange = rest_info['drange'])
            print rest.rest_name
            return (True, rest_info)

class Restaurant(models.Model):
    rest_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=255)
    services = models.CharField(max_length=255)
    vendors = models.ManyToManyField(Vendor, related_name="res")
    drange = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RestaurantManager()
