from random import *

def encrypt_message(password: str, message: str) -> str:
    """
    Cette fonction prend un mot de passe et un message en clair et renvoie le message crypté.

    Arguments:
    password -- le mot de passe utilisé pour crypter le message
    message -- le message en clair à crypter

    Renvoie:
    Le message crypté sous forme de chaîne de caractères
    """
    
    # Générer un entier aléatoire entre 50 et 150 inclus
    random_int = randint(50,150)
    # Convertir cet entier en caractère ASCII correspondant
    random_str = chr(random_int)

    # Calculer la valeur numérique du mot de passe
    password_value = 0
    password_cache = password
    while not password_cache == '' :
        password_value += ord(password_cache[0])
        password_cache = password_cache[1:]
    password_value += random_int

    # Crypter la longueur du message
    len_message = chr(len(message))
    # Crypter le message caractère par caractère
    encrypted_message_cache = ''
    index = 0
    message_cache = message
    while not message_cache == '':
        encrypted_message_cache += chr(ord(message_cache[0]) + password_value + index + random_int)
        message_cache = message_cache[1:]
        index += 1

    # Concaténer les différents éléments pour former le message crypté final
    encrypted_message = chr(password_value)
    encrypted_message += len_message
    encrypted_message += random_str
    encrypted_message += encrypted_message_cache

    # Renvoyer le message crypté
    return encrypted_message


def decrypt_message(password: str, encrypted_message: str) -> str:
    """
    Cette fonction prend un mot de passe et un message crypté et renvoie le message en clair correspondant.

    Arguments:
    password -- le mot de passe utilisé pour crypter le message
    encrypted_message -- le message crypté à décrypter

    Renvoie:
    Le message en clair correspondant sous forme de chaîne de caractères
    """
    
    # Extraire l'entier aléatoire utilisé pour le cryptage
    random_str = encrypted_message[2]
    random_int = ord(random_str)

    # Calculer la valeur numérique du mot de passe
    password_value = 0
    password_cache = password
    while not password_cache == '':
        password_value += ord(password_cache[0])
        password_cache = password_cache[1:]
    password_value = password_value + random_int

    # Vérifier que le mot de passe est correct
    if chr(password_value) == encrypted_message[0]:
        print('Your password is valid')
        # Extraire la longueur du message crypté
        len_encrypted_message = encrypted_message[1]
        # Extraire le message crypté
        encrypted_message_cache = encrypted_message[2:]
        # Décrypter le message caractère par caractère
        message_cache = ''
        index = 0
        while not encrypted_message_cache == '':
            message_cache += chr(ord(encrypted_message_cache[0]) - (index + password_value + random_int))
            encrypted_message_cache = encrypted_message_cache[1:]
            index += 1
        message = message_cache
        # Renvoyer le message en clair correspondant
        return message
    else :
        print('Your password is not valid')