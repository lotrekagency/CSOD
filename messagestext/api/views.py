from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from messagestext.models import MessageText
from messagestext.api.permissions import IsAuthorOrReadOnly
from messagestext.api.serializers import MessageTextSerializer

class MessageTextViewSet(viewsets.ModelViewSet):
    queryset = MessageText.objects.all()#.order_by("-created_at")
    lookup_field = "slug"
    serializer_class = MessageTextSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
