from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CustomTokenObtainPairView(TokenObtainPairView):
    """Класс представления для получения пары токенов."""

    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):
    """Класс представления для обновления токена доступа."""

    permission_classes = [AllowAny]
