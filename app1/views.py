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



#User signUp
def signUpView(request):
    #Create user code
    if  request.method =='POST': 
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirmPassword = request.POST.get('pass2')
        if password != confirmPassword:
            return HttpResponse("Your password and confirm password doesn't match")
        else:    
            myUser = User.objects.create_user(userName, email, password)
            myUser.save()
            return redirect('clickPicture')
        #User have been created
    return render(request, "signup.html")







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

  





#User Report
def reportView(request) :
    if request.method =='POST' :
        locate = request.POST.get('location')
        reason = request.POST.get('cause')
        extentDamage = request.POST.get('damage')
        description = request.POST.get('comments')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        # Do something with latitude and longitude  
        rep = report(location=locate, cause=reason, damage=extentDamage, comments=description, latitude=latitude,
          longitude=longitude)
        rep.save()
        return redirect('home')
    
    return render(request, "report.html")



def aboutView(request) :
    return render(request, "about.html")






#Adding Certification to User
def certificateView(request):
    restaurants = addRestaurentModel.objects.filter()
    args = {
        "restaurants": restaurants,  
    }
    return render(request, "certificate.html", args)



#Adding Certification from Admin 
def addRestaurentView(request):
    if request.method =='POST' :
        companyName = request.POST.get('company')
        issue = request.POST.get('issuedBy')
        expiry = request.POST.get('expiryDate')
        message = request.POST.get('details')

        #Exception handling
        if not companyName or not issue or not expiry or not message:
            return render(request, 'addRestaurent.html', {'error': 'All fields are required'})

        add = addRestaurentModel(commpanyName=companyName, issuedBy=issue, expiryDate=expiry, message=message)
        add.save()
        return redirect('dashboardView')
    return render(request, 'addRestaurent.html')









#GPS Tracking
def map(request, slug):
    map_obj = get_object_or_404(report, id=slug)
    latitude = map_obj.latitude
    longitude = map_obj.longitude
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Appending the search query for nearby lakes to the Google Maps URL
    google_maps_url += "&q=nearby river"
    return redirect(google_maps_url)
    






#Delete Certificate
def deleteCertificate(request, slug):
    delCertificate = addRestaurentModel.objects.get(id=slug)
    delCertificate.delete()

    return redirect('dashboardView')




#Resolving and Backlog
def resolve(request, slug):
    print(slug)
    if request.method == 'POST':
        teamName = request.POST.get('teamName')
        print(teamName)
    delReport = report.objects.get(id=slug)
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().time()
    log = f"Date: {current_date}, Time: {current_time}, Team name: {teamName}, solved the case report ID: {delReport.id}, location: {delReport.location}"
    history_entry = history(log=log)
    history_entry.save()
    
    delTeam = team.objects.get(name=teamName)
    
    delTeam.delete()
    
    delReport.delete()
    
    return redirect('dashboardView')

def log(request):
    log = history.objects.all()
    
    return render(request, 'log.html',{'log': log})



    
    

        
       
