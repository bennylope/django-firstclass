# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import random
from django.core.urlresolvers import reverse
from django.db import models, IntegrityError
from django_extensions.db.fields.json import JSONField


def key_gen():
    return '%04x' % random.getrandbits(40 * 4)


class Message(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    data = JSONField()

    def get_absolute_url(self):
        return reverse('view_message_online', kwargs={
            'key': self.key,
        })

    def save(self, *args, **kwargs):
        while not self.key:
            self.key = key_gen()
            try:
                super(Message, self).save(*args, **kwargs)
            except IntegrityError:
                self.key = None
            else:
                return

        super(Message, self).save(*args, **kwargs)

    def __str__(self):
        return "{} to {}".format(self.data['subject'], ', '.join(self.data['to']))
