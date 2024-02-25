# def normalize_ascii(letter):

def encrypt(plain, key):
    i = 0
    temp_cipher = 0
    cipher = ''
    while i < len(plain):
        for j in key:
            temp_cipher = ((ord(plain[i]) - 96) + (ord(j) - 96) - 1) % 26
            print(chr((temp_cipher) + 96))
            cipher += chr((temp_cipher) + 96)
            i += 1
            if i == len(plain):
               break
    print(cipher)
    
# def decrypt():
    
encrypt("thisplaintext", "sonysonysonys")