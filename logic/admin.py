from django.contrib import admin
from .models import Article, Feedback, Writer, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Feedback)
admin.site.register(Writer)
admin.site.register(Comment)