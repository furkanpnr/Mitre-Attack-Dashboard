from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('machines/', views.machines, name='machines'),
    path('attacks/', views.attacks, name='attacks'),
    path('results/', views.attack_results, name='results'),
    path('results/<int:id>', views.result_detail, name='result-detail')
]