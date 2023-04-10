from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home_view'),
    path('', include('pet_profile.urls')),
]
urlpatterns+=static(settings.STATIC_URL,
                    document_root=settings.STATIC_ROOT)