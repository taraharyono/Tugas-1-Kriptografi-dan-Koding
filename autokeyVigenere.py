def encrypt(plain, key):
    # lowering letters
    plain = plain.lower()
    plain = ''.join(char for char in plain if char.isalpha())
    key = key.lower()
    
    # initialization
    i = 0
    temp_cipher = 0
    cipher_text = ''
    
    # looping key
    for j in key:
        temp_cipher = (normalizeChar(plain[i]) + normalizeChar(j)) % 26
        temp_cipher += ord('a')
        cipher_text += chr(temp_cipher)
        i += 1
    
    # looping the rest of the text based on the plain text
    j = 0
    while i < len(plain):
        temp_cipher = (normalizeChar(plain[i]) + normalizeChar(plain[j])) % 26
        temp_cipher += ord('a')
        cipher_text += chr(temp_cipher)
        i += 1
        j += 1
        
    return cipher_text
    
def decrypt(cipher_text, key):
    # lowering letters
    cipher_text = cipher_text.lower()
    cipher_text = ''.join(char for char in cipher_text if char.isalpha())
    key = key.lower()
    
    # initialization
    i = 0
    temp_plain = 0
    plain_text = ''
    
    # looping key
    for j in key:
        temp_plain = (normalizeChar(cipher_text[i]) - normalizeChar(j)) % 26
        temp_plain += ord('a')
        plain_text += chr(temp_plain)
        i += 1
    
    # looping the rest of the text based on the plain text
    j = 0
    while i < len(cipher_text):
        temp_plain = (normalizeChar(cipher_text[i]) - normalizeChar(plain_text[j])) % 26
        temp_plain += ord('a')
        plain_text += chr(temp_plain)
        i += 1
        j += 1
        
    return plain_text


def normalizeChar(letter):
    n = ord(letter) - 97
    return n

# print(encrypt("negara penghasil minyak mentah di dunia", "indo"))
# print(decrypt("vrjoeeveegwefosmavjmszcndmlqbdbqqd", "indo"))

# while True:
#     plain_text = input("Enter the plaintext: ")
#     key = input("Enter the key: ")
#     cipher_text = encrypt(plain_text, key)
#     print("Encrypted Text:", cipher_text)