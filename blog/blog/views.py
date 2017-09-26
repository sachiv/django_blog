# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    queryset_list = Post.objects.all().order_by('-publish', 'id')

    paginator = Paginator(queryset_list, 25)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_list = paginator.page(paginator.num_pages)

    return render(request, "pages/home.html", {
        'post_list': post_list,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post_detail.html', {
        'post': post,
    })