from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserPhotoViewSet
from django.urls import path,include

router = DefaultRouter()

router.register('user', UserViewSet)
router.register('user-photo',UserPhotoViewSet)

urlpatterns = router.urls