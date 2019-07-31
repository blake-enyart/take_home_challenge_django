from ..models import Olympian
from rest_framework import serializers

class OlympianSerializer(serializers.ModelSerializer):
    total_medals_won = serializers.IntegerField()
    class Meta:
        model = Olympian
        fields = ("name",  "team", "age", "sport", "total_medals_won")
        read_only_fields = (
            'total_medals_won',
        )
