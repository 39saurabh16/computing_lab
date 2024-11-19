def rail_fence_encrypt(text, rails):
    rail = [[] for _ in range(rails)]
    direction_down = False
    row = 0

    for char in text:
        rail[row].append(char)
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(''.join(row) for row in rail)

def rail_fence_decrypt(cipher, rails):
    rail = [[] for _ in range(rails)]
    pattern = [0] * len(cipher)
    direction_down = False
    row = 0

    for i in range(len(cipher)):
        pattern[i] = row
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    pos = 0
    for r in range(rails):
        for i in range(len(cipher)):
            if pattern[i] == r:
                rail[r].append(cipher[pos])
                pos += 1

    result = []
    row = 0
    direction_down = False
    for i in range(len(cipher)):
        result.append(rail[row].pop(0))
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1

    return ''.join(result)

# Example
message = "Saurabh"
rails = 3
encrypted = rail_fence_encrypt(message, rails)
decrypted = rail_fence_decrypt(encrypted, rails)
print(f"Encrypted: {encrypted}, Decrypted: {decrypted}")
