from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, RegisterView

router = DefaultRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view()),
]
