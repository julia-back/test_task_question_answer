from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("forum/", include("question_answer.urls", namespace="question_answer")),
    # path("user/", include("users.urls", namespace="user")),
]
