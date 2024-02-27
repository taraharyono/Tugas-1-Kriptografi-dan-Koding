# Belajar codecademy

# Rumus enkripsi -> C = mP + b (mod 26)
def encrypt(plain_text, m, b):
    # isRelativePrime()
    # removing chars other than letters
    cipher_text = ''
    plain_text = plain_text.lower()
    plain_text = ''.join(char for char in plain_text if char.isalpha())
    
    # affine cipher calculation
    for i in plain_text:
        temp_cipher = (m*normalizeChar(i) + b) % 26
        temp_cipher += 97
        cipher_text += chr(temp_cipher)
        
    return cipher_text
    
    
# def decrypt(cipher_text, m, b):
    
#     return
    
# def isRelativePrime():
#     return 0

def normalizeChar(letter):
    n = ord(letter) - 97
    return n

print(encrypt("kripto", 7, 10))