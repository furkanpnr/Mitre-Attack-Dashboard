from django.urls import path
from . import views
# localhost:port/login -> login page
# localhost:port/singup -> singup page

urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
]
