# myapp/serializers.py
from rest_framework import serializers
from .models import Updates, LatestNews, OurTeam, BoardTeam

# Serializer for Updates
class UpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updates
        fields = ['id', 'image', 'title', 'description']

# Serializer for Latest News
class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = ['id', 'image', 'title', 'description']

# Serializer for Our Team
class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = ['id', 'image', 'name', 'role', 'description', 'twitter', 'instagram', 'linkedin']

# Serializer for Board Team
class BoardTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardTeam
        fields = ['id', 'name', 'twitter', 'instagram', 'linkedin']
