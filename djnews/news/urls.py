from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, 'news')


urlpatterns = [
    re_path('^',include(router.urls))   
]