from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def index(request):
    articles = Article.objects.all()
    context = {'name':articles}
    return render(request,'index.html',context)

def article(request):
    articles = Article.objects.all()
    context = {'name':articles}
    return render(request,'articles.html',context)



