from django.urls import path, include
from .views import *

urlpatterns = [
    path('',article_search, name="article_search"),
    path('create/',article_create),
    path('<int:id>/', article_detail, name="article_detail"),

]