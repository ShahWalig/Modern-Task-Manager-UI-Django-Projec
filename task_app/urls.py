from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('my_login', views.my_login, name="my_login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path("user-logout", views.user_logout, name="user_logout")

]