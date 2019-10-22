import locale
from rest_framework import serializers
from messagestext.models import MessageText, Answer

locale.setlocale(locale.LC_ALL, 'it_IT.utf8')  #questo ci consentirà di tradurre le date

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    user_has_voted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Answer
        exclude = ["messagetext", "voters", "updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance): #con questo metodo otterremo True o False a seconda che lo user abbia votato o meno
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()

class MessageTextSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField(read_only=True)
    user_has_answered = serializers.SerializerMethodField(read_only=True)
    cover = serializers.FileField(read_only=True, default="")

    class Meta:
        model = MessageText
        exclude =["updated_at"]

    def get_created_at(self, instance):
        return instance.created_at.strftime('%d %B %Y')

    def get_answers_count(self, instance):
        return instance.answers.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author= request.user).exists()
