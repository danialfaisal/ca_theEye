from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):

    class Meta:
            model = Events
            fields = ('pk','session_id', 'category', 'name', 'data', 'timestamp')