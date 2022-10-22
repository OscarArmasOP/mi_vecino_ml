from django.urls import path, include
from rest_framework import routers
from .views import MlView

router = routers.DefaultRouter()
router.register('ml', MlView, 'ml')

urlpatterns = router.urls