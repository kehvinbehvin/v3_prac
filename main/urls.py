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

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import LoginView, RegisterUsersView, UserListView, LogoutView
from custom.views import MessageListView, MessageCreateView


# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'first', FirstViewSet)
router.register(r'tweets', TweetsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/', DmView.as_view()),
    path('messages/<id>/<friend_id>', DmViewID.as_view()),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/login/',LoginView.as_view(),name='user-login'),
    path('user/signup/', RegisterUsersView.as_view(),  name='user-signup'),
    path('user/viewall/', UserListView.as_view(), name='user-all'),
    path('user/logout/',LogoutView.as_view(),name='user-logout')
    # path('messages/view/',MessageListView.as_view(), name='messages'),
    # path('messages/create/',MessageCreateView.as_view(), name='new_message'),
]
