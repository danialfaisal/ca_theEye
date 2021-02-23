from rest_framework import serializers
from .models import Events
from drf_writable_nested.serializers import WritableNestedModelSerializer


class EventSerializer(WritableNestedModelSerializer):
    data = serializers.JSONField()
    class Meta:
        model = Events
        fields = ('pk', 'session_id', 'category', 'data', 'name',  'timestamp')
