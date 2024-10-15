import random
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

 
def randomGenerator():
    while True:
        num = random.randint(9999999, 999999999)  
        if is_prime(num):
            return num

 
def is_primitive_root(g, n):
    required_set = {num for num in range(1, n) if gcd(num, n) == 1}
    actual_set = {pow(g, powers, n) for powers in range(1, n)}
    return required_set == actual_set

 
def find_primitive_root(n):
    for g in range(1, n):
        if is_primitive_root(g, n):
            return g
    return None


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


 
def findPow(base, exp, mod):
     
    result = 1
    for i in range(1,exp):
        result = (result*base)%mod
    return result

 
p = (int)(input("enter a prime number"))
 
# p = randomGenerator()  
print(f"Prime number is {p}")

primitive_root = find_primitive_root(p)
if primitive_root:
    print(f"Primitive root of prime number {p} is {primitive_root}")
else:
    print(f"No primitive root found for prime number {p}")
    exit()
 

#Alice_Private_key = random.randint(50, 100)
#print(f"Alice Private Key is {Alice_Private_key}")
Alice_Private_key = int(input("enter private key of Alice"))

#Bob_Private_Key = random.randint(50, 100)
#print(f"Bob Private Key is {Bob_Private_Key}")
Bob_Private_key = int(input("enter private key of Alice"))

 
Alice_Public_Key = findPow(primitive_root, Alice_Private_key, p)
print(f"Alice Public Key is {Alice_Public_Key}")

Bob_Public_Key = findPow(primitive_root, Bob_Private_key, p)
print(f"Bob Public Key is {Bob_Public_Key}")

 
common_Key1 = findPow(Bob_Public_Key, Alice_Private_key, p)
common_Key2 = findPow(Alice_Public_Key, Bob_Private_key, p)
print(f"Common key1 is {common_Key1}")

if common_Key1 == common_Key2:
    print("True - Alice and Bob have the same common key!")
else:
    print("False - Keys do not match.")