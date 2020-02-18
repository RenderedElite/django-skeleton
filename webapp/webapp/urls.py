from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from register import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
]
