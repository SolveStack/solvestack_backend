from django.contrib import admin

# Register your models here.
from .models import Term, StackNode
admin.site.register(Term)
admin.site.register(StackNode)