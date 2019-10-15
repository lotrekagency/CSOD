from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messagestext.api import views as mv  #mv = message view

router = DefaultRouter()
router.register(r"messagestext", mv.MessageTextViewSet)

urlpatterns = [
    path("", include(router.urls))
]
