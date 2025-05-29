from django.db import models
from django.utils import timezone
# Create your models here.
class CultureModel(models.Model):
    FestivalName=models.CharField(max_length=25)
    YourName=models.CharField(max_length=25)
    FestivalDetails=models.CharField(max_length=255)
    City=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Image=models.ImageField(upload_to='Images/')
    Date=models.DateTimeField(default=timezone.now)

class FoodModel(models.Model):
    FoodName=models.CharField(max_length=25)
    FoodlDetails=models.CharField(max_length=255)
    City=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Image=models.ImageField(upload_to='Images/')
    Date=models.DateTimeField(default=timezone.now)

class FolkDanceModel(models.Model):
    FolkDanceName=models.CharField(max_length=25)
    FolkDanceDetails=models.CharField(max_length=255)
    District=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Image=models.ImageField(upload_to='Images/')
    Date=models.DateTimeField(default=timezone.now)