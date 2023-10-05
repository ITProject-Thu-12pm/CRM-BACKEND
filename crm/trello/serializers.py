from rest_framework import serializers
from trello.models import Column, Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'content', 'priority', 'column']

class ColumnSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)  # This will nest the cards within a column.

    class Meta:
        model = Column
        fields = ['id', 'user', 'name', 'cards']  # 'cards' is added to show the related cards.