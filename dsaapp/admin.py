from django.contrib import admin
from .models import Content, Category, Question

# Register your models here.
admin.site.register(Content)
admin.site.register(Category)
admin.site.register(Question)