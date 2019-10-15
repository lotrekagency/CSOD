import locale
from rest_framework import serializers
from messagestext.models import MessageText

locale.setlocale(locale.LC_ALL, 'it_IT.utf8')

class MessageTextSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = MessageText
        exclude =["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')
