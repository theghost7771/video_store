from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework import routers

from .views import UserViewSet, VideoViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'videos', VideoViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token, name='get_api_token')
]
