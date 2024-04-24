from django.shortcuts import render,redirect
from .models import TourismModel
# Create your views here.
def main_view(request):
    return render(request,'OdishaTourismApp/index.html')

def add_blog(request):
    if request.method=='POST'and request.FILES.get('image'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        blog_content=request.POST['blog_content']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip']
        image = request.FILES['image'] 

        TourismModel.objects.create(
            FirstName=first_name,
            LastName=last_name,
            BlogContent=blog_content,
            City=city,
            State=state,
            Zip=zip,  # Corrected variable name
            Image=image
        )
        return redirect('main')
    else:
        return render(request,'OdishaTourismApp/index.html')

def latest_blog(request):
    data=TourismModel.objects.all()
    d={
        'data':data
    }
    return render(request,'OdishaTourismApp/latest_blog.html',d)