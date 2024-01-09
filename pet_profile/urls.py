from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from pet_profile import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("pet/photoupload/", views.PetPhotoUploadView.as_view(), name = "photo_upload"),
    path("owner/<slug:slug>/", views.PetOwnerDetailView.as_view(), name = "owner_profile"),
    path("pet/<slug:slug>/", views.PetDetailView.as_view(), name = "pet_profile"),
    path("pet_gallery/", views.PetPhotoListView.as_view(), name = "pet_gallery"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)