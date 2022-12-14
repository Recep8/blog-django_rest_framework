"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include,path
from rest_framework import routers
from article import views as article
from kullanici import views as register
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', article.UserViewSet)
router.register(r'groups', article.GroupViewSet)


urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('user-list/', include(router.urls)),
    path('', article.index, name='index'),
    path('admin/', admin.site.urls),
    path('article/', article.article),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register.register, name="register"),
    path('addarticle/', article.add_article),
    path('profile/', )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
