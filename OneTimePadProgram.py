import random


def generate_key(message):
    key = ''
    for char in message:
        key += chr(random.randint(0, 255))
    return key


def encrypt(message, key):
    encrypted_message = ''
    for i in range(len(message)):
        encrypted_message += chr(ord(message[i]) ^ ord(key[i]))
    return encrypted_message


message = input("enter your message ")
key = generate_key(message)
encrypted_message = encrypt(message, key)
print(f"your encrypted message is {encrypted_message}")
print(f"your key is {len(key)}")


def decrypt(encrypted_message, key):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        decrypted_message += chr(ord(encrypted_message[i]) ^ ord(key[i]))
    return decrypted_message


decrypted_message = decrypt(encrypted_message, key)
print(f"your decrypted message is {decrypted_message}")
