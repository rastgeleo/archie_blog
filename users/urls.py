from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # URL for profile page.
    path('profile/', views.profile, name='profile'),
    # URL for registration.
    path('register/', views.register, name='register'),
]
