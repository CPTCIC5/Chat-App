from rest_framework import serializers
from main.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id','author','text','created_at']
    

    """
    def create(self, validated_data):
        return Message.objects.create(author=self.context['request'].user,text=validated_data['text'])
    """
