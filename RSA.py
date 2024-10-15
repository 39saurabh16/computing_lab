
import random

def gcd(e,phi):
    while phi != 0:
        a = phi
        phi = e%phi
        e = a
    return a

def modInverse(a,m):
    for i in range(1,m):
       if (a*i)%m == 1:
           return i
    return -1

def encrypt(msg,e,n):
    result = 1
    for i in range(0,e):
        result = (result*msg)%n
    return result

def decrypt(cipher, d, n):
    result = 1
    for i in range(0,d):
      result = (result*cipher)%n
    return result


def generatePrime():
   
    while True:
       num = random.randint(50, 100)
       isprime = True
       for i in range(2,num):
          if num%i == 0:
             isprime = False
             break
     
       if isprime == True:
           return num     

 
p = generatePrime()
print(p)
q = generatePrime()
print(q)
while p==q:
    q = generatePrime()
n = p*q

phi = (p-1)*(q-1)
 

e=3
while(gcd(e,phi) != 1):
    e+=2
d = modInverse(e,phi)
print(f"Public key: (n={n}, e={e})")
print(f"Private key: (n={n}, d={d})")

message = int(input("enter a message to encrypt: "))
encrypted = encrypt(message,e,n)
print(f"Encrypted message is: {encrypted}")
decrypted = decrypt(encrypted,d,n)
print(f"Decrypted message is: {decrypted}")
