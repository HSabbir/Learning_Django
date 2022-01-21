
from django.http import HttpResponse

from articles.models import Article



def home(request):
    articles = Article.objects.get(id=2)

    TITLE = f"""<h1>{articles.title}"""
    CONTENT = f"""<h1>{articles.content}"""

    HTML_STRING = TITLE + CONTENT
    return HttpResponse(HTML_STRING)