# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title', 'slug', 'created', 'is_active', 'is_deleted']
    search_fields = list_display
