# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils import timezone


class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        return super(PostManager, self).filter(is_active=True, publish__lte=timezone.now(), is_deleted=False)

    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(is_active=True, is_deleted=False)
