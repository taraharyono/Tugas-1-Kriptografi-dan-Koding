# Belajar codecademy
import math

# Rumus enkripsi -> C = mP + b (mod 26)
def encrypt(plain_text, m, b):
    # isRelativePrime()
    # if isRelativePrime(m):
    
    # removing chars other than letters
    cipher_text = ''
    plain_text = plain_text.lower()
    plain_text = ''.join(char for char in plain_text if char.isalpha())
    
    print(plain_text)
    # affine cipher calculation
    for i in plain_text:
        temp_cipher = (m*normalizeChar(i) + b) % 26
        temp_cipher += ord('a')
        cipher_text += chr(temp_cipher)
        
    return cipher_text
    
    
def decrypt(cipher_text, m, b):
    # removing chars other than letters
    plain_text = ''
    cipher_text = cipher_text.lower()
    cipher_text = ''.join(char for char in cipher_text if char.isalpha())
    
    decrypt_key = findDecryptKey(m)
    # affine cipher calculation
    for i in cipher_text:
        temp_plain = (decrypt_key*(normalizeChar(i) - b)) % 26
        temp_plain += ord('a')
        plain_text += chr(temp_plain)
        
    return plain_text
    
def isRelativePrime(m):
    if (math.gcd(m, 26) == 1):
        return True
    else:
        return False
    
def findDecryptKey(m):
    found = False
    i = 0
    while (found == False):
        if ((i*m)%26 == 1):
            found = True
        else:
            i+=1
        
    return i

def normalizeChar(letter):
    n = ord(letter) - 97
    return n

print(encrypt("kriptoz", 7, 10))
print(decrypt("czolned", 7, 10))