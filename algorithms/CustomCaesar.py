class CaesarCipher:
    @staticmethod
    def encrypt(plaintext, shift):
        ciphertext = ""
        for char in plaintext:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                ciphertext += chr(shifted)
            else:
                ciphertext += char
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, shift):
        return CaesarCipher.encrypt(ciphertext, -shift)
