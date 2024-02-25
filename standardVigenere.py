# def normalize_ascii(letter):

def encrypt(plain, key):
    i = 0
    temp_cipher = 0
    cipher = ''
    plain = plain.lower()
    plain = plain.replace(" ", "")
    while i < len(plain):
        for j in key:
            temp_cipher = ((ord(plain[i]) - 96) + (ord(j.lower()) - 96) - 1) % 26
            if (temp_cipher == 0):
                temp_cipher = 26
            cipher += chr((temp_cipher) + 96)
            i += 1
            if i == len(plain):
               break
    return cipher
    
def decrypt(cipher, key):
    i = 0
    cipher = cipher.lower()
    cipher = cipher.replace(" ", "")
    temp_plain = 0
    plain = ''
    while i < len(cipher):
        for j in key:
            temp_plain = (ord(cipher[i]) - ord(j.lower())) % 26
            plain += chr(temp_plain + ord('a'))
            i += 1
            if i == len(cipher):
               break
    return plain
    # plain = plain.upper()

def separate(string):
    separated_string = ''
    for i in range(0, len(string), 5):
        separated_string += string[i:i+5] + ' '
    return separated_string.strip()

# print(encrypt("Dinas Pendidikan Kota Ternate", "selatsunda"))
# print(decrypt("VMYAL HYAGI VMVAG CIGDT WVYAM W", "selatsunda"))