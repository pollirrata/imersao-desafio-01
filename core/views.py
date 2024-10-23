from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views import View
from .models import Post, Tag


class BlogView(View):
    def get(self, request):
        context = dict(
            posts = Post.objects.all(),
            tags = Tag.objects.all()
        )

        return render(request, "admin/core/list_items.html", context)
