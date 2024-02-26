def extendedVigenereEncrypt(word, key):
    k = generateKey(word, key)
    processed_word = word.replace(" ", "")
    result = ""
    for i in range(len(processed_word)):
        c = (ord(processed_word[i]) + ord(k[i])) % 256
        result += chr(c)
    return result

def extendedVigenereDecrypt(word, key):
    k = generateKey(word, key)
    result = ""
    for i in range(len(word)):
        c = (ord(word[i]) - ord(k[i])) % 256
        result += chr(c)
    return result

def generateKey(word, k):
    length = len(k)
    if len(word) > length:
        for i in range(length, len(word)):
            k += k[i % length]
    return k