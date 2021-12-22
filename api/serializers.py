from rest_framework import serializers
from .models import Videos

class YoutubeAPISearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fileds = '__all__'
        exclude = ['created_at', 'updated_at']