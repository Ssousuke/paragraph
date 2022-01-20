from django.db import models

from authors.models import Author


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Articles(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    article = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artigo'
        verbose_name_plural = 'Artigos'
        ordering = ['-created_at']
