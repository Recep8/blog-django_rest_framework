from django.contrib import admin
from .models import Article
# Register your models here.

@admin.action(description="Mark selected articles copied")
def make_copy(modeladmin, request, queryset):
    for i in queryset:
        Article.objects.create(title=i.title, author=i.author, created_date=i.created_date,
                               content=i.content, upload_file=i.upload_file, tag=i.tag)
        print("Copy is created")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title", "author", "created_date","tag"]
    list_display_links = ["title", "created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    actions = [make_copy,]





    class Meta:
        model = Article


