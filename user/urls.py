from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import (
    CreateUserView,
    CreateTokenView,
    ManageUserView,
    EmailTokenObtainPairView,
)

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
