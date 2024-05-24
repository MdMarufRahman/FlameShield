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







#GPS Tracking
def map(request, slug):
    map_obj = get_object_or_404(report, id=slug)
    latitude = map_obj.latitude
    longitude = map_obj.longitude
    google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Appending the search query for nearby lakes to the Google Maps URL
    google_maps_url += "&q=nearby river"
    return redirect(google_maps_url)
    
def deleteContact(request, slug):
    certificate = contactUsModel.objects.get(id=slug)
    certificate.delete()

        # Appending the search query for nearby lakes to the Google Maps URL
    
    return redirect('displayContact')


   


#Available Teams
def addTeam(request):
    if request.method == 'POST':
        teamName = request.POST.get('name')  # Get the team name from the form
        # Create a new Team instance and save it to the database
        newTeam = team(name=teamName)
        newTeam.save()
        return redirect('addTeam')
    
    return render(request, 'availableteam.html', {'teams': team.objects.all()}) 


#Delete Team
def deleteTeam(request, slug):
    delTeam = team.objects.get(id=slug)
    delTeam.delete()

    return redirect('addTeam')


    

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



    
    

        
       
