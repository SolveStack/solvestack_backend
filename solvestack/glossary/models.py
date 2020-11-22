from django.db import models

from django_extensions.db.fields import ShortUUIDField


class Term(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    definition = models.TextField()

class TechnologyNode(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    definition = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255, blank=True)
    component = models.ForeignKey('Component', on_delete=models.SET_NULL, null=True, related_name='technologies')

class Component(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    definition = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255, blank=True)
    stack = models.ForeignKey('Stack', on_delete=models.CASCADE, related_name='components')

class Stack(models.Model):
    id = ShortUUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=80)
    definition = models.CharField(max_length=255)
    wikipedia_link = models.CharField(max_length=255, blank=True)
