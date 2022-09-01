from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.db.models import Q
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django.contrib import messages
from django.db.models.functions import TruncDate
from .forms import AddArticleForm



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

def index(request):
    articles = Article.objects.all()
    context = {'name':articles}
    return render(request,'index.html',context)

def article(request):
    if 'input_text' in request.GET:
        input_text = request.GET['input_text']
        articles = Article.objects.filter(Q(tag=input_text) | Q(title=input_text) | Q(author__username=input_text))
        dates = articles.annotate(date=TruncDate('created_date')).values('date')
        dates = dates.distinct()
        dates = dates.order_by("-date")
    else:
        articles = Article.objects.all()
        dates = articles.annotate(date=TruncDate('created_date')).values('date')
        dates = dates.distinct()
        dates = dates.order_by("-date")

    context={
            'input_text': articles,
            'date': dates,
    }

    return render(request, 'articles.html', context)

def add_article(request):
    context = {}

    form = AddArticleForm(request.POST or None, request.FILES or None,initial={'author': request.user})

    if form.is_valid():
        form.save()
        messages.success(request,  "Ekleme başarılı")


    context['form']=form
    return render(request, 'addarticle.html', context)

def delete_article(request):
    Article.objects.filter(id=id).delete()


def update_article(request):
    my_model_serializer = ArticleSerializer(
        instance=Article, data=validated_data)
    if my_model_serializer.is_valid():
        my_model_serializer.save()




