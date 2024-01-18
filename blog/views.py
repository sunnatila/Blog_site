from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article, Comment


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'


class PostDetailView(DetailView):
    model = Article
    template_name = 'post_detail.html'
    context_object_name = 'article'


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    template_name = 'post_new.html'
    fields = ['title', 'summary', 'body', 'image']
    context_object_name = 'article'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = 'post_edit.html'
    fields = '__all__'
    context_object_name = 'article'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'article'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['comment']

    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.article = Article.objects.get(pk=pk)
        form.instance.author = self.request.user
        return super().form_valid(form)


