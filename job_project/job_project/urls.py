"""
URL configuration for job_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from job_app import views as app_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app_views.main, name="main"),
    path("offers/", app_views.offers, name="offers"),
    path("offers/<int:offer_id>", app_views.offer, name="offer"),
    path("offers/<str:name>", app_views.category, name="category"),
    path("offers/add/", app_views.add_offer, name="new_offer"),
    path("register/", app_views.register, name="register"),
    path("delete<int:offer_id>", app_views.delete_offer, name="delete")
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", app_views.profile, name='profile')
]
