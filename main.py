from TableCipher import TableCipher

cipher = TableCipher("SECRET", size=6)

text = "HELLO WORLD"
encrypted = cipher.encrypt(text)
decrypted = cipher.decrypt(encrypted)

print(f"Исходный текст: {text}")
print(f"Зашифрованный: {encrypted}")
print(f"Дешифрованный: {decrypted}")