from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("auth_jwt.urls", namespace="auth_jwt")),
    path("forum/", include("question_answer.urls", namespace="question_answer")),
    # path("user/", include("users.urls", namespace="user")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="docs_redoc"),
]
