def autokey_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    
    # Extend the key using the plaintext
    extended_key = key + plaintext
    extended_key = extended_key[:len(plaintext)]

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(len(plaintext)):
        p_index = alphabet.index(plaintext[i])
        k_index = alphabet.index(extended_key[i])
        encrypted_text += alphabet[(p_index + k_index) % 26]

    return encrypted_text

def autokey_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    # Decrypt the ciphertext
    decrypted_text = ""
    for i in range(len(ciphertext)):
        c_index = alphabet.index(ciphertext[i])
        if i < len(key):
            k_index = alphabet.index(key[i])
        else:
            k_index = alphabet.index(decrypted_text[i - len(key)])
        decrypted_text += alphabet[(c_index - k_index) % 26]

    return decrypted_text

# Example Usage
plaintext = "HELLO WORLD"
key = "KEY"

encrypted_text = autokey_encrypt(plaintext, key)
decrypted_text = autokey_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
