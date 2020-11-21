from django.contrib import admin

# Register your models here.
from .models import Term, Stack
admin.site.register(Term)
admin.site.register(Stack)
