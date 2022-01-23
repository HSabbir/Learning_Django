from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail(request, id= None):
    article_object = None
    if id is not None:
        article_object = Article.objects.get(id=id)

    return render(request, 'article/details.html', {'article' : article_object})
