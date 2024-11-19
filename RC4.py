def ksa(key):
    """Key Scheduling Algorithm (KSA)"""
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S):
    """Pseudo-Random Generation Algorithm (PRGA)"""
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def rc4_encrypt_decrypt(data, key):
    """Encrypt or Decrypt data using RC4"""
    key = [ord(char) for char in key]  # Convert key to byte array
    S = ksa(key)  # Key Scheduling
    keystream = prga(S)  # Generate keystream
    result = bytearray()
    for byte in data:
        result.append(byte ^ next(keystream))  # XOR data with keystream
    return result

# Example Usage
key = "SECRET"
plaintext = "My name is Saurabh"

# Convert plaintext to bytes
plaintext_bytes = plaintext.encode()

# Encrypt
ciphertext = rc4_encrypt_decrypt(plaintext_bytes, key)
print(f"Ciphertext (hex): {ciphertext.hex()}")

# Decrypt (RC4 is symmetric, same function used for decryption)
decrypted_text = rc4_encrypt_decrypt(ciphertext, key).decode()
print(f"Decrypted Text: {decrypted_text}")
