from algorithms.CustomXOR import XOR as CustomXOR
from algorithms.CustomCaesar import CaesarCipher
from algorithms.CustomOneTimePad import OneTimePad
import tkinter.messagebox as messagebox

class EncryptionDecryption:
    @staticmethod
    def encrypt(plaintext, key, algorithm):
        try:
            if algorithm == "XOR (Exclusive OR)":
                ciphertext = CustomXOR.encrypt(plaintext, key)
            elif algorithm == "CAESER (Cipher)":
                ciphertext = CaesarCipher.encrypt(plaintext, int(key))
            elif algorithm == "One Time Pad (Cipher)":
                ciphertext = OneTimePad.encrypt(plaintext, key)
            else:
                return None
            return ciphertext
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    @staticmethod
    def decrypt(ciphertext_str, key, algorithm):
        try:
            if algorithm == "XOR (Exclusive OR)":
                plaintext = CustomXOR.decrypt(ciphertext_str, key)
            elif algorithm == "CAESER (Cipher)":
                plaintext = CaesarCipher.decrypt(ciphertext_str, int(key))
            elif algorithm == "One Time Pad (Cipher)":
                plaintext = OneTimePad.decrypt(ciphertext_str, key)
            else:
                return None
            return plaintext
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
