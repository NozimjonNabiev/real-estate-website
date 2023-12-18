from django.urls import path, include

from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("accounts", AccountViewSet)
router.register("elections", ElectionViewSet)
router.register("election-rooms", ElectionRoomViewSet)
router.register("candidates", CandidateViewSet)
router.register("votes", VoteViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]