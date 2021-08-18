from django.views.generic import ListView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Post, Author
from .forms import CommentForm


class IndexView(View):
    def get(self, request):
        posts = Post.objects.all().order_by("-date")[:3]
        author = Author.objects.get(id=1)
        context = {
            "posts": posts,
            "author": author,
        }
        return render(request, "blog/index.html", context)


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "posts"
    ordering = "-date"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm(),
          "comments": post.comments.all().order_by("-id")
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
          comment = comment_form.save(commit=False)
          comment.post = post
          comment.save()
          return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        else:           
            context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form(),
            "comments": post.comments.all().order_by("-id")
            }
            return render(request, "blog/post-detail.html", context)