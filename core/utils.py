import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6

def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))
    #genero una stringa a partire da una seriei di caratteri causuali in un range di 6
    #questa def la importeremo in .messagestext/signals.py
