import random

def is_prime(n):
    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_random_number(max_value):
     
    return random.randint(2, max_value)

def calculate_modulo_inverse(num, p):
     
    for i in range(1, p):
        if (num * i) % p == 1:
            return i
    return None   

 
p = int(input("Enter a large prime number (p): "))
if not is_prime(p):
    print(f"{p} is not a prime number. Exiting.")
    exit()

 
alpha = int(input(f"Enter a generator (alpha) for the group Z_{p}^*: "))
if not (1 < alpha < p):
    print(f"{alpha} is not a valid generator. Exiting.")
    exit()

 
bob_private_key = find_random_number(p - 2)
print("bobPrivateKey:", bob_private_key)

bob_public_key = pow(alpha, bob_private_key, p)
print("bobPublicKey:", bob_public_key)

alice_private_key = find_random_number(p - 2)
print("alicePrivateKey:", alice_private_key)

alice_public_key = pow(alpha, alice_private_key, p)
print("alicePublicKey:", alice_public_key)
 
masking_key = pow(bob_public_key, alice_private_key, p)
print("maskingKey:", masking_key)

 
message = int(input("Enter a number to encrypt: "))
print("message:", message)

 
cipher_text = (message * masking_key) % p
print("cipherText:", cipher_text)

 
new_masking_key = pow(alice_public_key, bob_private_key, p)
print("newMaskingKey:", new_masking_key)

 
modulo_inverse = calculate_modulo_inverse(new_masking_key, p)
print("moduloInverse:", modulo_inverse)

 
if modulo_inverse is not None:
    decrypted_message = (cipher_text * modulo_inverse) % p
    print("decryptedMessage:", decrypted_message)
else:
    print("No modular inverse exists; decryption failed.")
