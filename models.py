from django.db import models

# Create your models here.




class report(models.Model) :
    location = models.CharField(max_length=50)
    cause = models.CharField(max_length=50)
    damage = models.CharField(max_length=50)
    comments = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    
class addRestaurentModel(models.Model) :
    commpanyName = models.CharField(max_length=50)
    issuedBy = models.CharField(max_length=50)
    expiryDate = models.DateField()
    message = models.TextField()
    







