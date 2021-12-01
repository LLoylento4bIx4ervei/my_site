from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,  name='my_site-home'),
    path('about/', views.about_author, name='my_site-about_author')
]