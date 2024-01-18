from django.contrib import admin
from .models import Article, Comment


class CommentTabular(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentTabular]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
