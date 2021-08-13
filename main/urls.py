"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from direct_message.views import DmView, DmViewID
from django.contrib import admin
from django.urls import path, include
from first_app.views import FirstViewSet
from rest_framework import routers
from tweets.views import TweetsViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'first', FirstViewSet)
router.register(r'tweets', TweetsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('messages/', DmView.as_view()),
    path('messages/<id>/', DmViewID.as_view())
]
