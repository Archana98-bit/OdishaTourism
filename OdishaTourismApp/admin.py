from django.contrib import admin
from .models import CultureModel,FoodModel,FolkDanceModel
# Register your models here.
@admin.register(CultureModel)
class TourismModelAdmin(admin.ModelAdmin):
    list_display=['FestivalName','YourName']

@admin.register(FoodModel)
class TourismModelAdmin(admin.ModelAdmin):
    list_display=['FoodName']

@admin.register(FolkDanceModel)
class TourismModelAdmin(admin.ModelAdmin):
    list_display=['FolkDanceName']