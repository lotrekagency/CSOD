from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messagestext.api import views as mv  #mv = message view

router = DefaultRouter()
router.register(r"messagestext", mv.MessageTextViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("messagestext/<slug:slug>/answers/",
         mv.AnswerListAPIView.as_view(),
         name="question-answers-list"),

    path("messagestext/<slug:slug>/answer/",
         mv.AnswerCreateAPIView.as_view(),
         name="create-answer"),

    path("answers/<int:pk>/",
         mv.AnswerRUDAPIView.as_view(),
         name="answer-detail"),

    path("answers/<int:pk>/like/",
         mv.AnswerLikeAPIView.as_view(),
         name="answer-like")
]
