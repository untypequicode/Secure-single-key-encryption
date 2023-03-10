from random import *

def encrypt_message(password: str, message: str) -> str:
    password_value = 0
    random_int = randint(50,150)
    random_str = chr(random_int)
    password_cache = password
    while not password_cache == '' :
        password_value += ord(password_cache[0])
        password_cache = password_cache[1:]
    password_value += random_int
    encrypted_message = chr(password_value)

    message_cache = message
    len_message = chr(len(message_cache))
    encrypted_message_cache = ''
    index = 0
    while not message_cache == '':
        encrypted_message_cache += chr(ord(message_cache[0]) + password_value + index + random_int)
        message_cache = message_cache[1:]
        index += 1
    encrypted_message += len_message + random_str + encrypted_message_cache
    return encrypted_message


def decrypt_message(password: str, encrypted_message: str) -> str:
    pass

# Demande à l'utilisateur s'il veut crypter ou décrypter un message.
response = input("Do you want to encrypt or decrypt a message? (e/d) ")

if response.lower() == "e":
    # Cryptage du message.
    message = input("Enter the message you want to encrypt: ")
    password = input("Enter the password you want to use to encrypt the message: ")
    encrypted_message = encrypt_message(password, message)
    print(f"Your encrypted message is:'{encrypted_message}'")
    
elif response.lower() == "d":
    # Décryptage du message.
    encrypted_message = input("Enter the encrypted message you want to decrypt: ")
    password = input("Enter the password used to encrypt the message: ")
    decrypted_message = decrypt_message(password, encrypted_message)
    print("Your decrypted message is:", decrypted_message)
    
else:
    print("Invalid response.")