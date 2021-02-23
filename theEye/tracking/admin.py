from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventList(admin.ModelAdmin):
    model = Events
    list_display = ('session_id', 'category', 'name', 'data', 'timestamp')
    list_filter = ('session_id', 'category', 'timestamp')
    search_fields = ('session_id', 'category', 'timestamp')
    ordering = ['timestamp']
