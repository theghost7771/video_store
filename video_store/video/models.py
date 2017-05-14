# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse_lazy as rest_reverse_lazy


class Video(models.Model):
    title = models.CharField(_('Title'), max_length=500)
    aviable = models.BooleanField(_('Is aviable'), default=True)
    created = models.DateTimeField(auto_now_add=True)

    def rent_start(self):
        if self.aviable:
            self.aviable = False
            self.save()
            return True
        return False

    def rent_end(self):
        if not self.aviable:
            self.aviable = True
            self.save()
            return True
        return False
