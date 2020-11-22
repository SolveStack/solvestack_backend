from django.contrib import admin

# Register your models here.
from .models import Term, TechnologyNode, Component, Stack
admin.site.register(Term)
admin.site.register(Stack)
admin.site.register(Component)
admin.site.register(TechnologyNode)
