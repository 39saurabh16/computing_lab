def generate_numeric_key(key):
    # Generate a numeric key sequence from the key
    key_order = sorted(list(key))
    numeric_key = [key_order.index(char) + 1 for char in key]
    return numeric_key

def row_transposition_encrypt(plaintext, key):
    # Remove spaces and convert plaintext to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    numeric_key = generate_numeric_key(key)
    key_length = len(key)

    # Fill grid with plaintext, adding padding if needed
    grid = []
    for i in range(0, len(plaintext), key_length):
        row = plaintext[i:i + key_length]
        if len(row) < key_length:
            row += 'X' * (key_length - len(row))  # Padding
        grid.append(row)

    # Generate ciphertext by reading columns in the order of the numeric key
    ciphertext = ""
    for column_index in sorted(range(key_length), key=lambda k: numeric_key[k]):
        for row in grid:
            ciphertext += row[column_index]

    return ciphertext

def row_transposition_decrypt(ciphertext, key):
    # Remove spaces and convert ciphertext to uppercase
    ciphertext = ciphertext.replace(" ", "").upper()
    numeric_key = generate_numeric_key(key)
    key_length = len(key)
    num_rows = len(ciphertext) // key_length

    # Create an empty grid to store the reordered columns
    grid = [''] * key_length
    column_length = len(ciphertext) // key_length

    # Fill columns based on the numeric key
    current_index = 0
    for column_index in sorted(range(key_length), key=lambda k: numeric_key[k]):
        grid[column_index] = ciphertext[current_index:current_index + column_length]
        current_index += column_length

    # Read rows to reconstruct the plaintext
    plaintext = ""
    for i in range(num_rows):
        for column in grid:
            if i < len(column):
                plaintext += column[i]

    return plaintext.rstrip('X')  # Remove padding

# Example Usage
plaintext = "WE ARE DISCOVERED"
key = "ZEBRAS"

encrypted_text = row_transposition_encrypt(plaintext, key)
decrypted_text = row_transposition_decrypt(encrypted_text, key)

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
