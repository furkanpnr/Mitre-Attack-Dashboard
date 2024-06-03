from django.urls import path
from . import views

# localhost:port/ -> dashboard home
# localhost:port/home -> dashboard home

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
]