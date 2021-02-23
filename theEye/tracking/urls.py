from django.contrib import admin
from .models import Events

class _EventList(admin.ModelAdmin):
    list_display = ('session_id', 'category', 'name', 'data', 'timestamp')
    # list_filter = ('cust_number', 'name', 'city')
    # search_fields = ('cust_number', 'name')
    # ordering = ['cust_number']


admin.site.register(Events, _EventList)
