from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('status/', views.status, name='status'),
    path('register/', views.register, name='register'),
    path('accounts/', include('allauth.urls')),
]