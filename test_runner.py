import unittest
from TableCipher import TableCipher

class TestTableCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = TableCipher("SECRET", size=6)

    def test_encryption_decryption(self):
        text = "HELLO WORLD"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text.replace(" ", "").upper())

    def test_encrypt_non_alpha(self):
        text = "HELLO123!"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, "HELLO123!")

if __name__ == "__main__":
    unittest.main()