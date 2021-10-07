from django.urls import include, path
from rest_framework import routers

from users import views as user_views

router = routers.DefaultRouter()
router.register(r"create-user", user_views.UserCreateViewSet, basename="User")
router.register(r"users", user_views.UserViewSet, basename="User")
router.register(r"address", user_views.AddressViewSet, basename="Address")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "login/",
        user_views.MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
]
