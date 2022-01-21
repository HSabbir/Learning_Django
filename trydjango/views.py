
from django.shortcuts import render
from articles.models import Article



def home(request):
    articles = Article.objects.all()

    return render(request,'home.html',{'articles': articles})