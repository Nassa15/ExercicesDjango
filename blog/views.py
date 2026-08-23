from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def articleList(request):
    articles = Article.objects.all()

    response = ""

    for article in articles:
        response += f"{article.titre} : {article.contenu} : {article.date_publication}<br>"

    return HttpResponse(response)