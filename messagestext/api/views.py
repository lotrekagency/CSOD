from django.shortcuts import get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from messagestext.models import MessageText, Answer
from messagestext.api.permissions import IsAuthorOrReadOnly
from messagestext.api.serializers import MessageTextSerializer, AnswerSerializer

from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from messagestext.forms import MessageTextForm

IMAGE_FILE_TYPES= ['png', 'jpg', 'jpeg']

class MessageTextViewSet(viewsets.ModelViewSet):
    queryset = MessageText.objects.all().order_by("-created_at")
    lookup_field = "slug"
    serializer_class = MessageTextSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def create_cover(request):
        if request.method == 'POST':
            form = MessageTextForm(request.POST, request.FILES)
            if form.is_valid():
                message_cover = form.save(commit=False)
                message_cover.cover = request.FILES['cover']
                file_type = message_cover.cover.url.split('.')[-1]
                file_type = file_type.lower()
                if file_type not in IMAGE_FILE_TYPES:
                    return render(request, 'ERROR.html')
                message_cover.save()
                return render(request, 'Message.vue', {'message_cover': message_cover})
            context = {"form": form,}

class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        messagetext = get_object_or_404(MessageText, slug=kwarg_slug)

        # if messagetext.answers.filter(author=request_user).exists():
        #     raise ValidationError("hai già risposto a questo messaggio")

        serializer.save(author=request_user, messagetext=messagetext)

class MessageTextAnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(messagetext__slug=kwarg_slug)


class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user

        answer.voters.remove(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        user = self.request.user
        answer.voters.add(user)
        answer.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
