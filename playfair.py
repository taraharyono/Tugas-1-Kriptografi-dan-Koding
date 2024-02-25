def playfairEncrypt(msg, k):
    message = formatMessage(msg)
    key_matrix = playfairSquare(generateKey(k))
    result_bigram = []
    for i in range(len(message)):
        res = []
        pos1 = findInPlayfairSquare(key_matrix, message[i][0])
        pos2 = findInPlayfairSquare(key_matrix, message[i][1])
        ## same row
        if pos1[0] == pos2[0]:
            res.append(key_matrix[pos1[0]][(pos1[1]+1)%5])
            res.append(key_matrix[pos2[0]][(pos2[1]+1)%5])
        ## same column
        elif pos1[1] == pos2[1]:
            res.append(key_matrix[(pos1[0]+1)%5][pos1[1]])
            res.append(key_matrix[(pos2[0]+1)%5][pos2[1]])
        else:
            res.append(key_matrix[pos1[0]][pos2[1]])
            res.append(key_matrix[pos2[0]][pos1[1]])
        result_bigram.append(res)

        encrypted_message = ""
        for bigram in result_bigram:
            for char in bigram:
                encrypted_message += char

    return encrypted_message


def playfairDecrypt(msg, k):
    key_matrix = playfairSquare(generateKey(k))
    bigram = charToBigram(msg)
    result_bigram = []
    for i in range(len(bigram)):
        res = []
        pos1 = findInPlayfairSquare(key_matrix, bigram[i][0])
        pos2 = findInPlayfairSquare(key_matrix, bigram[i][1])
        ## same row
        if pos1[0] == pos2[0]:
            res.append(key_matrix[pos1[0]][(pos1[1]-1)%5])
            res.append(key_matrix[pos2[0]][(pos2[1]-1)%5])
        ## same column
        elif pos1[1] == pos2[1]:
            res.append(key_matrix[(pos1[0]-1)%5][pos1[1]])
            res.append(key_matrix[(pos2[0]-1)%5][pos2[1]])
        else:
            res.append(key_matrix[pos1[0]][pos2[1]])
            res.append(key_matrix[pos2[0]][pos1[1]])
        result_bigram.append(res)

    decrypted_message = ""
    for bigram in result_bigram:
        for char in bigram:
            decrypted_message += char
        
    return decrypted_message


def charToBigram(word):
    if len(word) % 2 == 0:
        bigram = [["" for i in range(2)] for i in range(len(word) // 2)]
        k = 0
        for i in range(len(word) // 2):
            for j in range(2):
                bigram[i][j] = word[k]
                k += 1
        return bigram

def generateKey(k):
    key = k.replace(" ", "").replace("j", "")
    unq_key = ""
    for i in range(len(key)):
        if key[i] not in unq_key:
            unq_key += key[i]
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) not in unq_key and chr(i) != "j":
            unq_key += chr(i)
    return unq_key

def playfairSquare(key):
    square = [["" for i in range(5)] for i in range(5)]
    k = 0
    for i in range(5):
        for j in range(5):
            square[i][j] = key[k]
            k += 1
    return square

def formatMessage(msg):
    message = msg.replace(" ", "").replace("j", "i")
    result = message
    for i in range(0, len(message), 2):
        if (i+1) != len(message):
            if message[i] == message[i+1]:
                result = message[:i+1] + "x" + message[i+1:]
    if len(result) % 2 == 1:
        result += "x"
    bigram = charToBigram(result)
    return bigram

def findInPlayfairSquare(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)