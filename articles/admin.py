from django.contrib import admin

from articles.models import Category, Articles

admin.site.register(Category)
admin.site.register(Articles)
