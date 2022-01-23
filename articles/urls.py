from django.urls import path, include
from .views import article_detail

urlpatterns = [
    path('<int:id>/', article_detail, name="article_detail")
]