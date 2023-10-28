from django.contrib import admin
from .models import Task


from django.utils import timezone

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('user', 'title','created_at','last_updated','due_date','priority')
    list_filter = ('user', 'created_at', 'last_updated','priority')
    search_fields = ('description', 'user__username', 'priority', 'created_at','last_updated')
    list_editable = ('due_date',)
    list_display_links = ('title',)
    actions = ('description',)


admin.site.register(Task,TaskAdmin)