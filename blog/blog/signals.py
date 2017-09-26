# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.dispatch import receiver
from django.db.models.signals import pre_save

from blog.core.utils import create_slug

from .models import Post


@receiver(pre_save, sender=Post, dispatch_uid="pre_save_post_receiver")
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """
    Create Post slug
    :param sender:
    :param kwargs:
    :return:
    """
    if not instance.slug:
        instance.slug = create_slug(instance)
