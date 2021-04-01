from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BehaviorViewSet, OriginatorViewSet

router = DefaultRouter()
router.register("behavior", BehaviorViewSet)
router.register("originator", OriginatorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
