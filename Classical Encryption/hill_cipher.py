def text_to_numbers(text):
    # Convert text to numbers (A=0, B=1, ..., Z=25)
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    # Convert numbers back to text
    return ''.join(chr(num + ord('A')) for num in numbers)

def matrix_multiply(matrix, vector, mod=26):
    # Multiply a matrix by a vector, mod 26
    result = []
    for row in matrix:
        value = sum(row[i] * vector[i] for i in range(len(vector))) % mod
        result.append(value)
    return result

def find_mod_inverse(a, m):
    # Find modular inverse of a under mod m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist")

def matrix_inverse(key_matrix, mod=26):
    # Compute the modular inverse of a 2x2 matrix mod 26
    determinant = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % mod
    determinant_inv = find_mod_inverse(determinant, mod)

    # Adjugate matrix
    adjugate = [
        [key_matrix[1][1], -key_matrix[0][1]],
        [-key_matrix[1][0], key_matrix[0][0]],
    ]

    # Multiply adjugate by determinant inverse, mod 26
    inverse_matrix = [[(determinant_inv * adjugate[i][j]) % mod for j in range(2)] for i in range(2)]
    return inverse_matrix

def hill_encrypt(plaintext, key_matrix):
    # Ensure plaintext length is a multiple of the matrix size
    matrix_size = len(key_matrix)
    if len(plaintext) % matrix_size != 0:
        plaintext += 'X' * (matrix_size - len(plaintext) % matrix_size)

    plaintext_numbers = text_to_numbers(plaintext)
    encrypted_numbers = []

    # Encrypt in blocks of size equal to the matrix size
    for i in range(0, len(plaintext_numbers), matrix_size):
        block = plaintext_numbers[i:i + matrix_size]
        encrypted_numbers.extend(matrix_multiply(key_matrix, block))

    return numbers_to_text(encrypted_numbers)

def hill_decrypt(ciphertext, key_matrix):
    matrix_size = len(key_matrix)
    inverse_key_matrix = matrix_inverse(key_matrix)

    ciphertext_numbers = text_to_numbers(ciphertext)
    decrypted_numbers = []

    # Decrypt in blocks of size equal to the matrix size
    for i in range(0, len(ciphertext_numbers), matrix_size):
        block = ciphertext_numbers[i:i + matrix_size]
        decrypted_numbers.extend(matrix_multiply(inverse_key_matrix, block))

    return numbers_to_text(decrypted_numbers)

# Example Usage
key_matrix = [
    [3, 3],
    [2, 5]
]  # Example 2x2 key matrix
plaintext = "HELLO"

# Encrypt and Decrypt
encrypted_text = hill_encrypt(plaintext, key_matrix)
decrypted_text = hill_decrypt(encrypted_text, key_matrix)

print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
