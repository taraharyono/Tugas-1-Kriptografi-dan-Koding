def extendedVigenereEncrypt(word, key):
    ## k = generateKey(word, key)
    processed_word = word.replace(" ", "")
    result = ""
    for i in range(len(processed_word)):
        k = key[i%len(key)]
        c = (ord(processed_word[i]) + ord(k)) % 256
        result += chr(c)
    return result

def extendedVigenereDecrypt(word, key):
    ## k = generateKey(word, key)
    result = ""
    for i in range(len(word)):
        k = key[i%len(key)]
        c = (ord(word[i]) - ord(k)) % 256
        result += chr(c)
    return result

def extendedVigenereEncryptBytes(byte_data, key):
    encrypted_bytes = bytearray()
    key_length = len(key)
    for i, byte in enumerate(byte_data):
        key_byte = ord(key[i % key_length])  # Convert character to ASCII value
        encrypted_byte = (byte + key_byte) % 256
        encrypted_bytes.append(encrypted_byte)
    return encrypted_bytes

def extendedVigenereDecryptBytes(byte_data, key):
    print(byte_data)
    decrypted_bytes = bytearray()
    key_length = len(key)
    for i, byte in enumerate(byte_data):
        key_byte = ord(key[i % key_length])  # Convert character to ASCII value
        decrypted_byte = (byte - key_byte) % 256
        decrypted_bytes.append(decrypted_byte)
    return decrypted_bytes