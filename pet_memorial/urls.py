from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home_view'),
    path('', include('pet_profile.urls')),
]