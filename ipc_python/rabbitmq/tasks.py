# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import

import time
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def add_slow_and_lazy(x, y):
    time.sleep(10)
    return x + y
