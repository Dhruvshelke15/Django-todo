# todo/admin.py
from django.contrib import admin
from .models import TodoItem, Tag

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'due_date', 'status')
    list_filter = ('status', 'timestamp')
    search_fields = ('title', 'description')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(TodoItem, TodoItemAdmin)
admin.site.register(Tag, TagAdmin)
