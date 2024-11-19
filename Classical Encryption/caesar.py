def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example
message = "Saurabh"
shift = 3
encrypted = caesar_cipher_encrypt(message, shift)
decrypted = caesar_cipher_decrypt(encrypted, shift)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")
