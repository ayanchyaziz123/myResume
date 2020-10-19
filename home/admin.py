from django.contrib import admin
from .models import Category, Project, Subject, HireMe

# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Subject)
admin.site.register(HireMe)