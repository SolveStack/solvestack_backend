from django.contrib import admin

# Register your models here.
from .models import Term, TechnologyNode
admin.site.register(Term)
admin.site.register(TechnologyNode)