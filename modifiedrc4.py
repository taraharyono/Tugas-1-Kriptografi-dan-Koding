def RC4(plaintext, key):
    # Inisialisasi S-box
    sbox = list(range(256))

    # Key-Scheduling Algorithm (KSA)
    j = 0
    for i in range(256):
        j = (j + sbox[i] + ord(key[i % len(key)])) % 256

        # Menggabungkan dengan konsep vigenere (sbox[i] ditambahkan dengan key)
        keyChar = ord(key[i % len(key)])
        sbox[i] = (sbox[i] + keyChar) % 256

        # Pertukarkan nilai sbox[i] dan sbox[j]
        temp = sbox[i]
        sbox[i] = sbox[j]
        sbox[j] = temp

    # Pseudo-random generation algorithm (PRGA) and encryption
    ciphertext = bytearray()
    i = 0
    l = 0
    for k in range(len(plaintext)):
        i = (i + 1) % 256
        l = (l + sbox[i]) % 256

        # Pertukarkan nilai sbox[i] dan sbox[l]
        temp = sbox[i]
        sbox[i] = sbox[l]
        sbox[l] = temp

        # Generate byte ke-k dari aliran
        t = (sbox[i] + sbox[l]) % 256
        keystreamByte = sbox[t]
        ciphertext.append(keystreamByte ^ ord(plaintext[k]))

    return bytes(ciphertext)

def RC4File(file, key):
    sbox = list(range(256))

    # Key-Scheduling Algorithm (KSA)
    j = 0
    for i in range(256):
        j = (j + sbox[i] + ord(key[i % len(key)])) % 256

        # Menggabungkan dengan konsep vigenere (sbox[i] ditambahkan dengan key)
        keyChar = ord(key[i % len(key)])
        sbox[i] = (sbox[i] + keyChar) % 256

        # Pertukarkan nilai sbox[i] dan sbox[j]
        temp = sbox[i]
        sbox[i] = sbox[j]
        sbox[j] = temp

    i = 0
    l = 0
    encryptedFile = bytearray(len(file))
    for k in range(len(file)):
        i = (i + 1) % 256
        l = (l + sbox[i]) % 256

        # Pertukarkan nilai sbox[i] dan sbox[l]
        temp = sbox[i]
        sbox[i] = sbox[l]
        sbox[l] = temp

        # Generate byte ke-k dari aliran
        t = (sbox[i] + sbox[l]) % 256
        keystreamByte = sbox[t]

        plainCharCode = file[k]
        encryptedByte = plainCharCode ^ keystreamByte
        encryptedFile[k] = encryptedByte

    return encryptedFile

# Contoh penggunaan
key = "wiu"
plaintext = "hilmibaskara"
print("Plaintext:", plaintext)

# Print Cipher Text
ciphertext = RC4(plaintext, key)
print("Ciphertext:", ciphertext)

# Print plain text balik
decryptedText = RC4(ciphertext, key)
print("Decrypted Text:", decryptedText.decode())
