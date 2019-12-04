from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_server import views

router = routers.DefaultRouter(views.FileViewSet)
router.register(r'file', views.FileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
