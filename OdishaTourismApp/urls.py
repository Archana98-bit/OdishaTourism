from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_view,name='main'),
    path('festival',views.festival_view,name='festival'),
    path('food',views.food_view,name='food'),
    path('Folk_Dance',views.Folk_Dance_view,name='Folk_Dance'),
    path('temple_page',views.temple_view,name='temple'),

]
