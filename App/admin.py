from django.contrib import admin
from .models import Way, Comment

# Register your models here.

class WayAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'content', 'date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'way')

admin.site.register(Way, WayAdmin)
admin.site.register(Comment, CommentAdmin)
