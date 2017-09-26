# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from model_utils.models import TimeStampedModel

from blog.core.behaviours import SlugMixin, StatusMixin

from .managers import PostManager


class Post(SlugMixin, StatusMixin, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
    title = models.CharField(_("Title"), max_length=255, null=False, blank=False)
    short_description = models.TextField(_("Short Description"), max_length=500, blank=True, )
    content = RichTextUploadingField(_("Content"), blank=True, null=True)
    publish = models.DateTimeField(_("Publish Date Time"), auto_now=False, auto_now_add=False, default=timezone.now)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
