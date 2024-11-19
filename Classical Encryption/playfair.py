def generate_key_matrix(key):
    # Remove duplicates, replace J with I, and prepare the key
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    combined = key + "".join(char for char in alphabet if char not in key)
    return [list(combined[i:i + 5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(text, key):
    # Prepare the text (replace J with I, handle repeated letters and odd length)
    text = text.upper().replace("J", "I")
    processed_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += text[i] + "X"
            i += 1
        elif i + 1 < len(text):
            processed_text += text[i] + text[i + 1]
            i += 2
        else:
            processed_text += text[i] + "X"
            i += 1

    # Generate the Playfair matrix
    matrix = generate_key_matrix(key)

    # Encrypt the text in pairs
    encrypted_text = ""
    for i in range(0, len(processed_text), 2):
        char1, char2 = processed_text[i], processed_text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            encrypted_text += matrix[row1][(col1 + 1) % 5]
            encrypted_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += matrix[(row1 + 1) % 5][col1]
            encrypted_text += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted_text += matrix[row1][col2]
            encrypted_text += matrix[row2][col1]

    return encrypted_text

def playfair_decrypt(text, key):
    # Generate the Playfair matrix
    matrix = generate_key_matrix(key)

    # Decrypt the text in pairs
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:  # Same row
            decrypted_text += matrix[row1][(col1 - 1) % 5]
            decrypted_text += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += matrix[(row1 - 1) % 5][col1]
            decrypted_text += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle rule
            decrypted_text += matrix[row1][col2]
            decrypted_text += matrix[row2][col1]

    return decrypted_text

# Example Usage
message = "Saurabh"
key = "KEYWORD"
encrypted_message = playfair_encrypt(message, key)
decrypted_message = playfair_decrypt(encrypted_message, key)

print(f"Message: {message}")
print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decrypted_message}")
