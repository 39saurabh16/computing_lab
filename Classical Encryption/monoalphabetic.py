import random

def generate_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return ''.join(shuffled)

def monoalphabetic_encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    encrypted = ""
    for char in text:
        if char.isalpha():
            encrypted += key[alphabet.index(char)]
        else:
            encrypted += char  # Keep non-alphabetic characters unchanged
    return encrypted

def monoalphabetic_decrypt(encrypted_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted = ""
    for char in encrypted_text:
        if char.isalpha():
            decrypted += alphabet[key.index(char)]
        else:
            decrypted += char  # Keep non-alphabetic characters unchanged
    return decrypted

# Example Usage
plaintext = "HELLO WORLD"
key = generate_key()

print(f"Generated Key: {key}")

encrypted_text = monoalphabetic_encrypt(plaintext, key)
decrypted_text = monoalphabetic_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
