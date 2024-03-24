from django.shortcuts import render
from django.http import HttpResponseRedirect


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


def loginPage(request):
    if ('email' in request.session):
        if('login' in request.session):
            return HttpResponseRedirect("/")
    request.session.flush()
    return render(request, 'base/login.html')


