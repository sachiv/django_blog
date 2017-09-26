# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ["title", "short_description", "content", "is_active"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content", ]
