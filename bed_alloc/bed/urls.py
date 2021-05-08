from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('status/', views.status, name='status'),
    path('register/', views.register, name='register'),
    path('staff_stat/', views.staff_stat, name='staff_stat'),
    path('accounts/', include('allauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()