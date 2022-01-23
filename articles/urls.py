from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:id>/', article_detail, name="article_detail"),
    path('',article_search)
]