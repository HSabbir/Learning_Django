from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Article
from .forms import ArticleForm

# Create your views here.
def article_detail(request, id= None):
    article_object = None
    if id is not None:
        article_object = Article.objects.get(id=id)

    return render(request, 'article/details.html', {'article' : article_object})

@login_required
def article_create(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid() :
        article_obj = form.save()
        context["form"] = ArticleForm()
        # context["created"] = True
        # print(context)

    return render(request,'article/create.html', context)

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