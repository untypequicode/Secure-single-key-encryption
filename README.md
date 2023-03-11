# SecureEncryption

This Python module provides two functions, **encrypt_message()** and **decrypt_message()**, for encrypting and decrypting messages using a password.

## Usage

The program prompts the user to choose whether they want to encrypt or decrypt a message. If they choose to encrypt, they enter the message they want to encrypt and a password. The program then encrypts the message using the password and displays the encrypted message. If they choose to decrypt, they enter the encrypted message and the password that was used to encrypt it. The program then decrypts the message and displays the decrypted message.

## Functions

The **encrypt_message()** function takes a password and a message as input and returns the encrypted message as a string.

The **decrypt_message()** function takes a password and an encrypted message as input and returns the decrypted message as a string.

## Dependencies

This program requires the **random** module to generate random integers used for encryption.

## Examples
<p align="center">
  <img src="doc/SecureEncryption.gif" alt="SecureEncryption" width=75%"/>
</p>
