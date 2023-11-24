
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from home.Viewset import UserViewSet
from home.Viewset import ContactViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
