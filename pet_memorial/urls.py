from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('pet_profile.urls')),
    path('home/', views.HomeView.as_view(), name='home_view')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    print("SECURITY WARNING: Keep the secret key used in production secret!\nSECURITY WARNING: Don't run with debug turned on in production!")
    