from django.db import models

import shortuuid


class Term(models.Model):
    id = shortuuid.ShortUUID()
    name = models.CharField(max_length=80)
    definition = models.TextField()
