from random import randint

def encrypt_message(password: str, message: str) -> str:
    """
    Fonction pour crypter un message.
    """
    # Calcul de la somme de la valeur de chaque caractère du mot de passe.
    password_sum = sum(ord(char) for char in password)

    # Calcul du message crypté.
    encrypted_message = ""
    for char in message:
        char_value = ord(char) + password_sum + len(encrypted_message) + 1
        encrypted_message += chr(char_value)

    # Formatage du message crypté.
    random_int = randint(50, 150)
    formatted_encrypted_message = chr(password_sum % 26 + 97)
    formatted_encrypted_message += chr(len(message))
    formatted_encrypted_message += chr(random_int)
    formatted_encrypted_message += encrypted_message

    return formatted_encrypted_message

def decrypt_message(password: str, encrypted_message: str) -> str:
    """
    Fonction pour décrypter un message.
    """
    # Récupération du caractère qui indique la somme de la valeur de chaque caractère du mot de passe.
    password_sum_char = encrypted_message[0]
    password_sum = ord(password_sum_char) - 97

    # Récupération de la longueur du message.
    message_length_char = encrypted_message[1]
    message_length = ord(message_length_char)

    # Récupération du caractère aléatoire.
    random_int_char = encrypted_message[2]
    random_int = ord(random_int_char)

    # Récupération du message crypté.
    encrypted_message = encrypted_message[3:]
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        char_value = ord(char) - password_sum - i - 1 - random_int
        decrypted_message += chr(char_value)

    return decrypted_message

# Demande à l'utilisateur s'il veut crypter ou décrypter un message.
response = input("Do you want to encrypt or decrypt a message? (e/d) ")

if response.lower() == "e":
    # Cryptage du message.
    message = input("Enter the message you want to encrypt: ")
    password = input("Enter the password you want to use to encrypt the message: ")
    encrypted_message = encrypt_message(password, message)
    print("Your encrypted message is:", encrypted_message)
    
elif response.lower() == "d":
    # Décryptage du message.
    encrypted_message = input("Enter the encrypted message you want to decrypt: ")
    password = input("Enter the password used to encrypt the message: ")
    decrypted_message = decrypt_message(password, encrypted_message)
    print("Your decrypted message is:", decrypted_message)
    
else:
    print("Invalid response.")
