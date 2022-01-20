from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    profile = models.ImageField(upload_to='author/profile', blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.user_name}'

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autor'
        ordering = ['-created_at']
