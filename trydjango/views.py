
from django.shortcuts import render
from articles.models import Article



def home(request):
    articles = Article.objects.get(id=2)

    return render(request,'home.html',{'articles': articles})