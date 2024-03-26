from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

# Rejestracja widoków w routerze
router.register(r'comments', CommentViewSet)
router.register(r'disability_types', DisabilityTypeViewSet)
# router.register(r'ratings/<int:pk>', RatingViewSet.as_view({"put": "put"}, name='rating-update'))
router.register(r'ratings', RatingViewSet)
router.register(r'places', PlaceViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-autch", include("rest_framework.urls", namespace="rest_framork"))
]
