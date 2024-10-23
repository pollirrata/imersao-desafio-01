from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from core.models import Post, Tag


admin.site.register(Post)
admin.site.register(Tag)
