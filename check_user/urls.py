from django.urls import path,include
from .views import UserTokenViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()

route.register('',viewset=UserTokenViewSet)

urlpatterns = [
    path('user',include(route.urls))
]