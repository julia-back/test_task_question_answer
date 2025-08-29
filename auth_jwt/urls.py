from django.urls import path
from .apps import AuthJwtConfig
from . import views


app_name = AuthJwtConfig.name


urlpatterns = [
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", views.CustomTokenRefreshView.as_view(), name="token_refresh"),
]
