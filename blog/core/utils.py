# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from random import choice
from string import digits

from django.utils.text import slugify


def create_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        try:
            slug = slugify(instance.title)
        except:
            slug = slugify(instance.name)
    qs = instance.__class__.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, ''.join(choice(digits) for i in range(5)))
        return create_slug(instance, new_slug=new_slug)
    if len(slug) > 254:
        if qs.first():
            length = len(str(qs.first().id))
            nb_chars = 254 - length
            slug = slug[:nb_chars] + qs.first().id
        else:
            slug = slug[:254]
    if not slug:
        slug = ''.join(choice(digits) for i in range(5))
    return slug
