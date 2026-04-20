# Module Lab: Caesar Cipher Program Bug #3

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    # Di sini kita menghitung kunci untuk mundur (negatif)
    decryptKey = -1 * int(cipherKey)
    # BUG DI BARIS INI:
    return encryptMessage(message, cipherKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    myMessage = getMessage()
    myCipherKey = getCipherKey()
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()