from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pet_profile.urls')), #pet_profiles urls should be prioritized before home because it is more specific and will match fewer objects/queries #though this could change
    path('home/', views.HomeView.as_view(), name='home_view'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    print("SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = '1eovl-=7pwb6e1*c7y@6@s7n0+ig)mxos2im3b_+^%3+rdze&k'\nSECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True")
    