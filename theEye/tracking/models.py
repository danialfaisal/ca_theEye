from datetime import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone

from jsonfield import JSONField


class Events(models.Model):
    session_id = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    data = models.JSONField(default="{}")
    name = models.CharField(max_length=100)

    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-timestamp"]
        unique_together = [
            ["category", "name"],
        ]

