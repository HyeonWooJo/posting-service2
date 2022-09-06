from django.db import models

from core.models import TimeStampModel


class Posting(TimeStampModel):
    title   = models.CharField(max_length=20)
    context = models.CharField(max_length=200)
    psword  = models.CharField(max_length=60)

    class Meta:
        db_table = "postings"