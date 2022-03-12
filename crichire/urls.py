"""crichire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers
from registrations import views as Register
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from accounts.views import MyTokenObtainPairView
from coaches import views as Coach
from players import views as Player

router = DefaultRouter()
router.register(r'register', Register.RegistrationViewSet)
router.register(r'training', Coach.TrainingViewSet)
router.register(r'player', Player.PlayerViewSet)
router.register(r'playerstats', Player.Player_StatsViewSet)
router.register(r'fixtures', Player.FixtureViewSet)
router.register(r'complete-player', Player.CompletePlayerViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/', include('accounts.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  
]



         
