class OneTimePad:
    @staticmethod
    def encrypt(plaintext, key):
        ciphertext = ""
        for i in range(len(plaintext)):
            char = plaintext[i]
            key_char = key[i % len(key)]
            ciphertext += chr((ord(char) + ord(key_char)) % 256)  
        return ciphertext

    @staticmethod
    def decrypt(ciphertext, key):
        plaintext = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            key_char = key[i % len(key)]
            decrypted_char = chr((ord(char) - ord(key_char)) % 256)  
            plaintext += decrypted_char
    
        plaintext = plaintext[:-1]
        
        return plaintext
