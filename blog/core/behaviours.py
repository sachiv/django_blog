# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _


class StatusMixin(models.Model):
    is_active = models.BooleanField(_("active"), default=True, blank=False, null=False)
    is_deleted = models.BooleanField(_("deleted"), default=False, blank=False, null=False)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(blank=True, null=True, max_length=255)

    class Meta:
        abstract = True
