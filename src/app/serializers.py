from rest_framework import serializers
from app.models import VisionBoard

class VisionBoardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    images = serializers.ListField(child=serializers.CharField())
    class Meta:
        model=VisionBoard
        fields='__all__'
    
    def create(self, validated_data):
        return VisionBoard.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.images = validated_data.get('images', instance.images)
        instance.save()
        return instance