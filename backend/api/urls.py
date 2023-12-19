from django.urls import path, include

from .views import *

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("agents", AgentsViewSet)
router.register("customers", CustomersViewSet)
router.register("contact-info", ContactInfoViewSet)
router.register("licenses", LicensesViewSet)
router.register("reviews", ReviewsViewSet)
router.register("estates", EstateViewSet)
router.register("amenities", AmenitiesViewSet)
router.register("contracts", ContractsViewSet)
router.register("favorites", FavoritesViewSet)
router.register("posts", PostsViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]