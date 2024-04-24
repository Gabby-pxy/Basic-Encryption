class XOR:
    @staticmethod
    def encrypt(plaintext, key):
        ciphertext = ""
        for i in range(len(plaintext)):
            char = plaintext[i]
            key_char = key[i % len(key)]
            if char != '\n':  
                ciphertext += chr(ord(char) ^ ord(key_char))
            else:
                ciphertext += '\n'  
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        plaintext = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            key_char = key[i % len(key)]
            if char != '\n': 
                plaintext_char = chr(ord(char) ^ ord(key_char))
            else:
                plaintext_char = '\n'  
            plaintext += plaintext_char
        return plaintext