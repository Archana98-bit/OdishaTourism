from django.urls import path
from . import views
urlpatterns = [
    path('',views.main_view,name='main'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('latest_blog',views.latest_blog,name='latest_blog'),
]
