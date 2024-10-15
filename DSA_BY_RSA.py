import math

def is_prime(num):
     
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def gcd(a, b):
    
    while b != 0:
        a, b = b, a % b
    return a

def input_checking(prompt):
     
    while True:
        num = int(input(prompt))
        if num > 100 and is_prime(num):
            return num
        else:
            print(f"{num} is not a prime number or less than 100.")

def relatively_prime_e(phi_n):
     
    while True:
        e = int(input("Enter e: "))
        if gcd(e, phi_n) == 1:
            return e
        else:
            print(f"{e} is not relatively prime to phi_n = {phi_n}.")

def mod_inverse(e, phi_n):
     
    for d in range(1, phi_n):
        if (e * d) % phi_n == 1:
            return d
    return None

def text_to_numbers(text):
    
    return [ord(char) for char in text]

def numbers_to_text(numbers):
     
    return ''.join([chr(num) for num in numbers])
 
p = input_checking("Enter p: ")
q = input_checking("Enter q: ")
n = p * q
phi_n = (p - 1) * (q - 1)

e = relatively_prime_e(phi_n)
d = mod_inverse(e, phi_n)

public_key = (e, n)
private_key = (d, n)

print(f"\nPublic Key: {public_key}")
print(f"Private Key: {private_key}")

 
message = input("\n[Sender] Enter the message to sign: ")
message_numbers = text_to_numbers(message)

 
signature = [pow(num, d, n) for num in message_numbers]
print(f"[Sender] Signature: {signature}")

 
print("\n[Sender] Sending the message and signature to the receiver...")
 
tamper_message = input("\n Do you want to tamper with the message? (y/n): ")
if tamper_message.lower() == 'y':
    tampered_message = input("[Receiver] Enter a tampered message: ")
    message_numbers = text_to_numbers(tampered_message)

 
print("\n[Receiver] Verifying the signature...")
verified_numbers = [pow(sig, e, n) for sig in signature]
verified_message = numbers_to_text(verified_numbers)

if verified_message == numbers_to_text(message_numbers):
    print("[Receiver] Signature is valid. Message integrity verified.")
    print(f"[Receiver] Verified Message: {verified_message}")
else:
    print("[Receiver] Signature is invalid. Message may have been tampered with.")