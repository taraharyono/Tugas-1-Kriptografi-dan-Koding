import standardVigenere

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
        
    # read result by row
    encrypted_text = ""
    for j in range(column_key):
        for row in result:
            if j < len(row):
                encrypted_text += row[j]
    
    return encrypted_text

def columnar_transposition_decrypt(cipher_text, column_key):
    num_rows = len(cipher_text) // column_key
    
    matrix = [[0 for _ in range(column_key)] for _ in range(num_rows)]

    i = 0
    for j in range(column_key):
        for k in range(num_rows):
            matrix[k][j] = cipher_text[i]
            i += 1
            if (i == len(cipher_text)):
                break
    
    decrypted_text = ''
    for j in range(num_rows):
        for k in range(column_key):
            decrypted_text += matrix[j][k]
    
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

print(encrypt("departemen teknik informatika itb", 6, "sony"))
print(decrypt("vrcsaskbmycwvjnybiagjganlhcbrp", 6, "sony"))