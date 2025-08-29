from django.urls import path

from . import views
from .apps import AuthJwtConfig

app_name = AuthJwtConfig.name


urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", views.CustomTokenRefreshView.as_view(), name="token_refresh"),
]
