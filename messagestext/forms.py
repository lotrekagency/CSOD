from django import forms
from .models import MessageText

class MessageTextForm(forms.ModelForm):

    class Meta:
        models = MessageText
        fields = [
            'created_at',
            'updated_at',
            'content',
            'slug',
            'author',
            'cover',
        ]
