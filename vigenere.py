def extendedVigenereEncrypt(word, key):
    k = generateKey(word, key)
    result = ""
    for i in range(len(word)):
        c = (ord(word[i]) + ord(k[i])) % 256
        result += chr(c)
    print(result)

def extendedVigenereDecrypt(word, key):
    k = generateKey(word, key)
    result = ""
    for i in range(len(word)):
        c = (ord(word[i]) - ord(k[i])) % 256
        result += chr(c)
    print(result)

def generateKey(word, k):
    length = len(k)
    if len(word) > length:
        for i in range(length, len(word)):
            k += k[i % length]
    return k