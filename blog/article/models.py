from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="Başlık")
    author = models.ForeignKey("auth.User", verbose_name="Yazar", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    upload_file = models.ImageField(upload_to="images/", null=True, blank=True)
    tag = models.CharField(max_length=50, default="Deneme")

    def __str__(self):
        return self.title

