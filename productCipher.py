import standardVigenere
import math

def columnar_transposition_encrypt(plaintext, column_key):
    plaintext = plaintext.replace(" ", "")
    
    result = []
    i = 0
    # make column
    while i < len(plaintext):
        a = []
        for j in range (column_key):
            a.append(plaintext[i])
            i += 1
            if (i == len(plaintext)):
                break
        result.append(a)
    for row in result:
        for element in row:
            print(element, end=" ")  # Print the element with a space separator
        print()  #   
         
    # read result by row
    encrypted_text = ""
    for j in range(column_key):
        for row in result:
            if j < len(row):
                encrypted_text += row[j]
    
    return encrypted_text

def columnar_transposition_decrypt(cipher_text, column_key):
    print("decrypt")
    num_rows = column_key
    num_column = math.ceil(len(cipher_text) / num_rows)

    result = []
    i = 0
    # make column
    while i < len(cipher_text):
        a = []
        for j in range (num_column):
            a.append(cipher_text[i])
            i += 1
            if (i == len(cipher_text)):
                break
        result.append(a)
            
    for row in result:
        for element in row:
            print(element, end=" ")  # Print the element with a space separator
        print()  #
        
    decrypted_text = ''
    for j in range(num_column):
        for row in result:
            if j < len(row):
                decrypted_text += row[j]
    
    return decrypted_text        

def encrypt(plain_text, column_key, vigenere_key):
    # vigenere cipher
    encrypted_text = standardVigenere.encrypt(plain_text, vigenere_key)
    
    # transposition cipher
    encrypted_text = columnar_transposition_encrypt(encrypted_text, column_key)
    
    return encrypted_text

def decrypt(cipher_text, column_key, vigenere_key):
    decrypted_text = columnar_transposition_decrypt(cipher_text, column_key)
    
    decrypted_text = standardVigenere.decrypt(decrypted_text, vigenere_key)
    
    return decrypted_text

# columnar_transposition_encrypt("departemen teknik informatika itb", 6)
# columnar_transposition_decrypt("dekfiemnokpeiraankmirtiattentb", 6)

# print(encrypt("departemen teknik informatika itb", 6, "sony"))
# print(decrypt("vrcsaskbmycwvjnybiagjganlhcbrp", 6, "sony"))
# print(columnar_transposition_encrypt("masterpieces", 3))
# print(columnar_transposition_decrypt(columnar_transposition_encrypt("masterpieces", 3), 3))
# harusnya ini meearcspetis

