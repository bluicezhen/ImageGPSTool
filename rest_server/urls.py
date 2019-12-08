from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_server.views import FileViewSet

router = routers.DefaultRouter()
router.register(r'file', FileViewSet)
# router.register(r'qiniu/token', QiniuTokenViewSet, base_name="qiniu_token")


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
