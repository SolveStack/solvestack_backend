from django.db import models

from django_extensions.db.fields import ShortUUIDField


class Term(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    definition = models.TextField()
