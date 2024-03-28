from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

import random
import string
from datetime import datetime



#firebase lib
import pyrebase

# Create your views here.


#firebase Database Configaretion
config = {
  "apiKey": "AIzaSyCSCJVxNn8N28Hpxt2SuBQz2-HyqMFAeH8",
  "authDomain": "testproject-24d54.firebaseapp.com",
  "databaseURL": "https://testproject-24d54-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "testproject-24d54",
  "storageBucket": "testproject-24d54.appspot.com",
  "messagingSenderId": "865886225620",
  "appId": "1:865886225620:web:30a7aa1f51f6239bede741"
}
 
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()



def main(request):
    if 'email' and 'login' in request.session:
        user_id = request.session.get("localid")
        user_info = database.child('user').child(user_id).get().val()
        if user_info:
            pass_data = {
                "user_id":user_id,
                "username":user_info['username'],
                "full_name":user_info['full_name'],
                "email":user_info['email'],
                "role":user_info['role']
            }
        return render(request, 'base/main.html',{'user_data':pass_data})
    request.session.flush()
    return HttpResponseRedirect("/login/")



def index(request):
    if 'email' and 'login' in request.session:
        return render(request, 'base/main.html')
    request.session.flush()
    return HttpResponseRedirect("/login/")


def loginPage(request):
    if 'email' in request.session:
        if'login' in request.session:
            return HttpResponseRedirect("/")
    request.session.flush()
    return render(request, 'base/login.html')


def registerPage(request):
    if 'email' in request.session:
        if'login' in request.session:
            return HttpResponseRedirect("/")
    request.session.flush()
    return render(request, 'base/register.html')
        

# def forgetpassPage(request):
#     if 'email' in request.session:
#         if'login' in request.session:
#             return HttpResponseRedirect("/")
#     request.session.flush()
#     return render(request, 'base/forgetpassPage.html')


def postsignin(request):
    if 'register_user' in request.POST:
        full_name = request.POST.get("name").strip()
        username = request.POST.get("username").strip()
        email = request.POST.get("email").strip()
        password = request.POST.get("password").strip()
        confirmpassword = request.POST.get("confirm_password").strip()
        error = False
        if password != confirmpassword:
            messages.warning(request, 'password not matched')
            error = True
        if len(password) < 8:
            messages.warning(request, "Password is too short")
            error = True
        if len(full_name) == 0:
            messages.warning(request, "Full name is Empty")
            error = True
        if len(username) == 0:
            messages.warning(request, "Username is Empty")
            error = True
        if len(email) == 0:
            messages.warning(request, "Email is Empty")
            error = True
        if error == False:
            try:
                ret_val = auth.create_user_with_email_and_password(email,password)
            except:
                messages.warning(request,"User alrady exist")
                return HttpResponseRedirect("/register/")
            now =  datetime.now()
            pass_data = {
                "full_name": full_name, 
                "username": username, 
                "email": email, 
                "role": 1, 
                "approved": 0,
                "created_at": datetime.timestamp(now)
                }
            database.child("user").child(ret_val["localId"]).set(pass_data)
            # messages.set_level(request,level=25)
            messages.success(request,'User Created Successfully. Please use creds for login.')
            return HttpResponseRedirect('/login/')
        return HttpResponseRedirect("/register/")
    
    elif "login" in request.POST:
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            ret_val = auth.sign_in_with_email_and_password(email, password)
        except:
            messages.warning(request, 'Credentials error.')
            return HttpResponseRedirect('/login/')
        user_id  = ret_val['localId']
        try:
            user_info_ret = database.child('user').child(user_id).get()
        except:
            request.session.flush()
            messages.warning(request, 'Credentials error.')
            return HttpResponseRedirect('/login/')
        
        user_info = user_info_ret.val()
        if user_info['approved'] != 0:
            messages.warning(request, "Please wait for approvel from Admin.")
            return HttpResponseRedirect('/login/')
        request.session['login'] = True
        request.session['name'] = user_info["full_name"]
        request.session['email'] = email
        request.session['role'] = user_info["role"]
        request.session['localid'] = user_id
        return HttpResponseRedirect('/')
    
    elif "forgetpass" in request.POST:
        email = request.POST.get("email")
        try:
            ret_val = auth.send_password_reset_email(email)
            messages.success(request, 'Please check your mail for resetting password.')
            return HttpResponseRedirect("/")
        except:
            messages.warning(request, 'Credentials error.')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

def logout(request):
    request.session.flush()
    messages.success(request, 'Logout Successfully')
    return HttpResponseRedirect('/login/')



def create_blog(request):

    def generate_random_id(length=16):
        characters = string.ascii_letters + string.digits
        random_id = ''.join(random.choice(characters) for i in range(length))
        return random_id
    
    if 'email' and  'login'  in request.session:
        if 'blog_post' in request.POST:
            user_id = request.session['localid']
            blog_id = generate_random_id()
            blog_title = request.POST.get("title").strip()
            blog_body = request.POST.get("body").strip()
            date = datetime.now()
            pass_data = {
                    "blog_title": blog_title, 
                    "blog_body": blog_body,
                    "created_at": datetime.timestamp(date)
                    }
            database.child("blog").child(user_id).child(blog_id).set(pass_data)
            return HttpResponseRedirect('/createblog/')
        
    return render(request, 'base/createblog.html')
