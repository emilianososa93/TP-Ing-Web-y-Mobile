from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)
from .models import *


def foro(request):
    contenido = {'Posts': Post.objects.all()}
    return render(request, 'Foro/Foro.html', contenido)


class PostListView(ListView):
    model = Post  # Use the Post model
    template_name = 'Foro/Foro.html'  # Use this view instead of the default one
    context_object_name = 'Posts'  # Be referred to as "Post", as indicated in "contenido"
    ordering = ['-date_posted']  # Show newer posts first
    paginate_by = 5


class UserPostListView(ListView):
    model = Post  # Use the Post model
    template_name = 'Foro/user_post.html'  # Use this view instead of the default one
    context_object_name = 'Posts'  # Be referred to as "Post", as indicated in "contenido"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailedView(DetailView):
    model = Post  # Use the Post model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['context'] = Comment.objects.filter()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from posting
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post  # Use the Post model
    fields = ['title', 'text']

    def form_valid(self, form):  # Check to stop non logged users from posting
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # Use the Post model
    success_url = '/foro'

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment  # Use the Comment model
    fields = ['post', 'text']
    success_url = '/foro'

    def form_valid(self, form):  # Check to stop non logged users from commenting
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment  # Use the Comment model
    fields = ['text']
    success_url = '/foro'

    def form_valid(self, form):  # Check to stop non logged users from commenting
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment  # Use the Comment model
    success_url = '/foro'

    def test_func(self):  # Check to stop non authors from updating
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
