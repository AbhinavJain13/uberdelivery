from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


# Create your models here.
class UserManager(models.Manager):
    def mail(self,email):
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
           server = smtplib.SMTP('smtp.gmail.com', 587)
           fromaddr = "newdelivery6@gmail.com"
           toaddr = email
           msg = MIMEMultipart()
           msg['From'] = fromaddr
           msg['To'] = toaddr
           msg['Subject'] = "Python email"
           code="333333"
           body = "Python test mail"+code
           msg.attach(MIMEText(body, 'plain'))
           server.ehlo()
           server.starttls()
           server.ehlo()
           text = msg.as_string()
        #    try:
        #        server.login("newdelivery6@gmail.com", "newdelivery")
        #        server.sendmail(fromaddr, toaddr, text)
        #        server.quit()
        #    except SMTPRecipientsRefused:
           server.login("newdelivery6@gmail.com", "newdelivery")
           server.sendmail(fromaddr, toaddr, text)
           server.quit()
           info={
           'email':email,
           'code':code,
           }
           return (True,info)
           print "email sent"

    def validate(self,param):
        errors=[]
        # user=User.objects.filter(email=param['email'])
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(param['f_name'])<1 and len(param['f_name'])<3:
            errors.append("firstname cannot be blank or less then 3")
        if len(param['l_name'])<1 and len(param[l_name])<3:
            errors.append("lastname cannot be blank or less than 3")
        if not EMAIL_REGEX.match(param['email']) and len(param['email'])<1:
            errors.append("invalid email or email cannot be blank")
        if len(param['addr'])<1:
            errors.append("address cannot be blank")
        if len(param['apt'])<1:
            errors.append("apt/house cannot be blank")
        if len(param['city'])<1:
            errors.append("city cannot be blank")
        if len(param['state'])<1:
            errors.append("state cannot be blank")
        if len(param['zipcode'])<1:
            errors.append("zipcode cannot be blank")
        if len(param['phone'])<10:
            errors.append("phone cannot be blank or less than 10 digits")
        if len(param['password'])<1:
            errors.append("password cannot be blank")
        if not param['cpassword']==param['password']:
            errors.append("password and confirm password do not match")
        # if user>0:
        #     errors.append("email already exist")
        if len(errors)>0:
            return(False,errors)
        else:
            #call the mailing function
            email1=self.mail(param['email'])
            pass2=param['password']
            pass3=pass2.encode()
            hashed= bcrypt.hashpw(pass3,bcrypt.gensalt())
            this_address=Address.objects.create(addr=param['addr'],apt=param['apt'],city=param['city'],state=param['state'],zipcode=param['zipcode'])
            user=self.create(f_name=param['f_name'],l_name=param['l_name'],email=param['email'],code=email1[1]['code'],valid="False",password=hashed)
            user.address.add(this_address)
            return(True,user)
    def login(self,user):
        print user
        user_log=self.filter(email=user['email'])
        if user_log and user_log[0].valid==True:
            print user_log
            pass2=user['password']
            pass3=pass2.encode()
            if bcrypt.hashpw(pass3,user_log[0].password.encode())== user_log[0].password:
                print user_log[0].id
                return {'user':user_log[0]}
            # else:
        return{'error':"email or password failed"}

class Address(models.Model):
    addr=models.CharField(max_length=50)
    apt=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=5)
class User(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    code=models.CharField(max_length=6)
    valid=models.BooleanField(default=False)
    address=models.ManyToManyField(Address,related_name="useraddress")
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=255)

    objects=UserManager()
