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

        if not re.match(PHONE_REGEX, vendor_info['phone']):
            errors.append("Enter a valid phone format eg:123 456 7890")

        if len(vendor_info['password']) < 8:
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
            return(True, True)

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
            return(True, True)



class Restaurant(models.Model):
    rest_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    cuisine = models.CharField(max_length=255)
    services = models.CharField(max_length=255)
    drange = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RestaurantManager()
