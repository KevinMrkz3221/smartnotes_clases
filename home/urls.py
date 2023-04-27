from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('Logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('register', views.SingUpView.as_view(), name='register'),
]

