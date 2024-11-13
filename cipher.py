# add your code here
def caesar_cipher(plain_text, shift=5):
    encrypted_text = ""

    for char in plain_text:
        
        if char.isupper():
            
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        elif char.islower():
            
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            
            encrypted_text += char

    return encrypted_text
plain_text = input("Please provide a sentence to encrypt: ")
encrypted_text = caesar_cipher(plain_text, shift=5)

print("Encrypted text:", encrypted_text)
