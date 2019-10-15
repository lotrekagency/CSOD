from django.db.models.signals import pre_save #un segnale che viene emesso prima che un'istanz venga salvata
from django.dispatch import receiver
from django.utils.text import slugify #permette di generare no slug a partire da un testo

from core.utils import generate_random_string
from messagestext.models import MessageText

#sotto stiamo creando una funzione che richiamiamo alla ricezione del segnale
#viene richiamata da pre_save e da parte del MessageText
@receiver(pre_save, sender=MessageText)   #stiamo, cosi facendo, aggiungendo uno slug in base alla domanda in se
def add_slug_to_message(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string
#come ottenere degli slug unici? aggiungiamo a questo slug una string di caratteri casuali. VEDI
#.core/utils.py

#una volta importato generate_random_string dobbiamo concludere il settaggio su messagestext/__init__.py
