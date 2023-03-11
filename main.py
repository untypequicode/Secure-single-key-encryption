from SecureEncryption import *

# Demande à l'utilisateur s'il veut crypter ou décrypter un message.
response = input("Do you want to encrypt or decrypt a message? (e/d) ")

if response.lower() == "e":
    # Cryptage du message.
    message = input("Enter the message you want to encrypt: ")
    password = input("Enter the password you want to use to encrypt the message: ")
    encrypted_message = encrypt_message(password, message)
    print(f"Your encrypted message is: '{encrypted_message}'")
    
elif response.lower() == "d":
    # Décryptage du message.
    encrypted_message = input("Enter the encrypted message you want to decrypt: ")
    password = input("Enter the password used to encrypt the message: ")
    decrypted_message = decrypt_message(password, encrypted_message)
    print(f"Your decrypted message is: '{decrypted_message}'")
    
else:
    print("Invalid response.")