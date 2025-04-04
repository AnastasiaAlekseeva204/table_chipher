import math

def get_order(key):
    return sorted(range(len(key)), key=lambda x: key[x])

def encrypt(message, key):
    message = message.replace(" ", "").upper()
    cols = len(key)
    rows = math.ceil(len(message) / cols)
    padded = message.ljust(rows * cols, 'X')

    table = [padded[i:i+cols] for i in range(0, len(padded), cols)]

    order = get_order(key)
    cipher = ''
    for col in order:
        for row in table:
            cipher += row[col]
    return cipher

def decrypt(cipher, key):
    cols = len(key)
    rows = math.ceil(len(cipher) / cols)
    total_cells = rows * cols
    padded_cipher = cipher.ljust(total_cells, 'X')
    table = [[''] * cols for _ in range(rows)]
    order = get_order(key)

    k = 0
    for col in order:
        for row in range(rows):
            table[row][col] = padded_cipher[k]
            k += 1

    plaintext = ''.join(''.join(row) for row in table)
    return plaintext.rstrip('X')