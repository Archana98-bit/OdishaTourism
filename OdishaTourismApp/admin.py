from django.contrib import admin
from .models import TourismModel
# Register your models here.
@admin.register(TourismModel)
class TourismModelAdmin(admin.ModelAdmin):
    list_display=['FirstName','LastName']