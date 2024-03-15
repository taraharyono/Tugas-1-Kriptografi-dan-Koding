import base64

# Key-Scheduling Algorithm
def KSA(key):
    # inisialisasi larik
    sbox = list(range(256))
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i % len(key)]) % 256
        # Pertukarkan nilai sbox[i] dan sbox[j]
        sbox[i], sbox[j] = sbox[j], sbox[i]
    return sbox

# Pseudo-random generation algorithm (PRGA)
def PGRA(sbox, length):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        keystream_byte = sbox[(sbox[i] + sbox[j]) % 256]
        keystream.append(keystream_byte)
    return keystream

# Enkripsi RC4
def rc4_encrypt(text, key):
    # KSA
    sbox = KSA(key)
    # PRGA
    keystream = PGRA(sbox, len(text))
    encrypted_text = bytearray()
    for i in range(len(text)):
        encrypted_text.append(text[i] ^ keystream[i])
    return encrypted_text

# Dekripsi RC4
def rc4_decrypt(encrypted_text, key):
    return rc4_encrypt(encrypted_text, key)  # Dekripsi dan Enkripsi sama saja

plaintext = "hilmibaskara"
key = "wiu"

plaintext_bytes = plaintext.encode()
key_bytes = key.encode()

encrypted_text = rc4_encrypt(plaintext_bytes, key_bytes)
print("Encrypted text:", encrypted_text)

encrypted_text_base64 = base64.b64encode(encrypted_text)

print("Encrypted text (Base64):", encrypted_text_base64.decode())

decrypted_text = rc4_decrypt(encrypted_text, key_bytes)
print("Decrypted text:", decrypted_text.decode())