# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'slug', 'publish', 'created', 'is_active', 'is_deleted']
    search_fields = list_display


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['content', 'created', 'is_active', 'is_deleted']
    search_fields = list_display
