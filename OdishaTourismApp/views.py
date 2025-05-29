from django.shortcuts import render,redirect
from .models import CultureModel,FoodModel,FolkDanceModel
def main_view(request):

    if request.method=='POST'and request.FILES.get('image'):
        FestivalName=request.POST['first_name']
        YourName=request.POST['last_name']
        FestivalDetails=request.POST['blog_content']
        city=request.POST['city']
        state=request.POST['state']
        image = request.FILES['image'] 

        CultureModel.objects.create(
            FestivalName=FestivalName,
            YourName=YourName,
            FestivalDetails=FestivalDetails,
            City=city,
            State=state,
            Image=image
    )
        return redirect('main')
   
    else:
        return render (request,'OdishaTourismApp/index.html')

def mueseum_view(request):
    return render(request,'OdishaTourismApp/mueseum.html')
def festival_view(request):
        data=CultureModel.objects.all()
        d={
        'data':data
        }
        return render(request,'OdishaTourismApp/festivals.html',d)

def food_view(request):
        if request.method=='POST' and request.FILES.get('image'):
            FoodName=request.POST['food_name']
            FoodDetails=request.POST['food_details']
            city=request.POST['city']
            state=request.POST['state']
            image = request.FILES['image'] 

            FoodModel.objects.create(
                 FoodName=FoodName,
                 FoodlDetails=FoodDetails,
                 City=city,
                 State=state,
                 Image=image,
            )
            data=FoodModel.objects.all()
            d={
                'data':data
            }
            return render(request,'OdishaTourismApp/food.html',d)
      
        else:
            data=FoodModel.objects.all()
            d={
                'data':data
            }
            return render(request,'OdishaTourismApp/food.html',d)
           
def Folk_Dance_view(request):
     if request.method=='POST' and request.FILES.get('image'):
            Folk_Dance_Name=request.POST['Folk_Dance_Name']
            Folk_Dance_Details=request.POST['Folk_Dance_Details']
            District=request.POST['District']
            state=request.POST['state']
            image = request.FILES['image'] 

            FolkDanceModel.objects.create(
                 FolkDanceName=Folk_Dance_Name,
                 FolkDanceDetails=Folk_Dance_Details,
                 District=District,
                 State=state,
                 Image=image,
            )
            data=FolkDanceModel.objects.all()
            d={
                'data':data
            }
            return render(request,'OdishaTourismApp/FolkDance.html',d)
     else:
        data=FolkDanceModel.objects.all()
        d={
                'data':data
        }
        return render(request,'OdishaTourismApp/FolkDance.html',d)

def temple_view(request):
    return render(request,'OdishaTourismApp/temple.html')

