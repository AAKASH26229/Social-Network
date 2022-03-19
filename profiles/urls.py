from django.urls import path, include
from . import views


urlpatterns = [
    path('connections/', views.profileConnectionView, name="connections"),
    path('connection/confirm/<id>/', views.confirmConnection, name="confirm_connection"),
    path('<id>/', views.profileDetail, name="profile_detail"),
    path('', views.profileView, name="profile"),
]
