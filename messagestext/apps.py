from django.apps import AppConfig


class MessagesTextConfig(AppConfig):
    name = 'messagestext'

    def ready(self):
        import messagestext.signals
