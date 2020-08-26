from django.db import models

from oscar.apps.payment.models import *  # noqa isort:skip

from django_extensions.db.models import TimeStampedModel


class PaypalOrder(TimeStampedModel):
    details = models.TextField(blank=False)
    order_id = models.CharField(
        max_length=255,
        blank=False,
        unique=True)

    class Meta:
        app_label = 'payment'
