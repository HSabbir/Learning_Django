from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail(request, id= None):
    article_object = None
    if id is not None:
        article_object = Article.objects.get(id=id)

    return render(request, 'article/details.html', {'article' : article_object})


def article_search(request):
    query_dict = request.GET

    try:
        query = int(query_dict.get('q'))
    except:
        query = None

    query_obj = None
    if query is not None:
        query_obj = Article.objects.get(id=query)

    return render(request, 'article/search.html',{'article':query_obj})