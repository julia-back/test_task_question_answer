from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):

    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):

    permission_classes = [AllowAny]
