from rest_framework import serializers
from event.models import Event
from datetime import datetime

class CustomDateField(serializers.DateField):
    def to_representation(self, value):
        # Check if the date is None or missing
        if not value:
            return None  # or you can return a default value or string like "N/A" if needed

        # Format date to '01-01-2010' format
        return value.strftime('%d-%m-%Y')

class EventSerializer(serializers.ModelSerializer):
    start = CustomDateField()
    end = CustomDateField()

    class Meta:
        model = Event
        fields = ['id', 'user', 'title', 'start', 'end']
        read_only_fields = ['user']
    
    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        return event