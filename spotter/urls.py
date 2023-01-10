"""spotter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from spotterapi.views.auth import login_user, register_user
from spotterapi.views.exercise_view import ExerciseView
from spotterapi.views.session_view import SessionView
from spotterapi.views.plan_view import PlanView
from spotterapi.views.profile_view import ProfileView


router = DefaultRouter(trailing_slash = False)

router.register(r'exercises', ExerciseView, "exercise")
router.register(r'sessions', SessionView, "session")
router.register(r'plans', PlanView, "plan")
router.register(r'profiles', ProfileView, "profile")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls))
]
