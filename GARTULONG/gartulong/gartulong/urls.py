# urls.py

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="homepage"),  # No .html extension
    path('login/', views.login_page, name="login"),  # No .html extension
    path('signup/', views.signup_page, name="signup"),  # No .html extension

    
]
