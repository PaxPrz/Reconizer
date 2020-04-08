from django.urls import path, include

from . import views

urlpatterns = [
    # path("login/", views.login_user, name="login"),
    path("register/", views.register, name="register"),
    # path("logout/", views.logout, name="logout"),
    path("", include("django.contrib.auth.urls")),
]