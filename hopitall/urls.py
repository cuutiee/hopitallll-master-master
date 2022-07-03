
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('doctors/', views.doctors, name="doctors"),
    path('login_sign/', views.login_sign, name="login_sign"),
    path('login_sign/authentification/<int:id>', views.authentification, name="authentification"),
    path('login_sign/authentification/profile/<int:id>', views.profile, name="profile"),
    path('login_sign/authentification/profile/<int:id>/appointment/', views.appointment, name="appointment"),
    path('login_sign/authentification/profile/<int:id>/appointements/', views.appointements, name="appointements"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)