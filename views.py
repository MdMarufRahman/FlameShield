import base64
import datetime
import os
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from app1.models import contactUs as contactUsModel, report, addRestaurentModel, report, picture, TestUser, team, history
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .decorators import unauthenticated_user, admin_only


# Create your views here.

def homeView(request) :
    return render(request, "home.html")



def viewHomepage(request) :
               
    return render(request, "index.html") 











#User Authentication
def loginView(request) :
    if  request.method == 'POST' :
        loginName = request.POST.get('logName')
        loginPass = request.POST.get('logPass')
        
        user = authenticate(request,username = loginName, password = loginPass )
        if loginName == "admin":
            if user is not None :
                login(request, user)
                return redirect('dashboardView')
            else:
                return HttpResponse("Username or Password is incorrect")  
        else:   
            if user is not None :
                login(request, user)
                return redirect('faceRecog')
            else:
                return HttpResponse("Username or Password is incorrect") 
        
    return render(request, "index.html")     

  

#Contact Us Page
def contactUs(request) : 
    if request.method =='POST' :
        fullName = request.POST.get('full_name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        en = contactUsModel(contactFullName=fullName, contactEmail=email, contactPhoneNumber=phoneNumber, contactSubject=subject, contactMessage=message)
        en.save()
        return redirect('homepage')
        
    return render(request, "contact.html")

def safetyView(request) :
    return render(request, "safety.html")

#Contact Display
def displayContactView(request):
    contacts = contactUsModel.objects.filter()
    
    args = {
        "contacts": contacts,  
    }
    return render(request, "contactAdmin.html",args)


#Contact Display
def clickPicture(request):
    last_object =User.objects.latest('id') 
    last_object_user=last_object.username
    
    if request.method=="POST":
        img=request.POST.get("img_data")
        picture_obj = picture.objects.create(
            userName=last_object_user,
            img=img
        )
        picture_obj.save()
        return redirect('home')
           
    return render(request, "face.html")






 



    




    
    

        
       
