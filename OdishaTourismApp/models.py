from django.db import models
from django.utils import timezone
# Create your models here.
class TourismModel(models.Model):
    FirstName=models.CharField(max_length=25)
    LastName=models.CharField(max_length=25)
    BlogContent=models.CharField(max_length=255)
    City=models.CharField(max_length=25)
    State=models.CharField(max_length=25)
    Zip=models.IntegerField()
    Image=models.ImageField(upload_to='Images/')
    Date=models.DateTimeField(default=timezone.now)