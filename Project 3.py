abc = []

def vigenereCipher():
    vTable = []

    # Generates a vigenere table and sets it to 'vTable'.
    def vigenereTableGen():
        for count, i in enumerate(abc):
            tempList = []
            for j in abc:
                charIndex = ord(abc[ord(j) - 97])
                if charIndex + count > 122:
                    charIndex -= 26
                tempList.append(chr(charIndex + count))
            vTable.append(tempList)

    # Makes the length of the key equal to the length of the encryted text.
    # Does this by repeating the key for the length of the encryted text.
    def keyLength(text, key):
        if not len(text) == len(key):
            for x in range(len(text) - len(key)):
                if x > len(key):
                    x -= len(key)
                key += key[x]
        return key

    # Takes inputs from the user, then ciphers the user-inputted text.
    # It does this by looping for the length of the text and converting
    # the current character from both the user-inputted text and
    # the string returned by the 'keyLength' method into indexes of abc.
    # Once it has the indexes, it uses them along with the vTable list
    # to generate a new character which is then appended to
    # the 'encryptedText' string.
    def main():
        encryptedText = ''
        decryptedText = ''
        key = ' '
        text = 'abcdefg'
        # text = input('Enter what you want to cipher.\n')
        #  input('Enter a keyword (no spaces).\n')
        while ' ' in key:
            key = keyLength(text, 'no')
        
        def encrypt(encryptedText):
            for count, x in enumerate(text):
                charIndex = ord(x.lower()) - 97
                if charIndex >= 0:
                    encryptedText += vTable[charIndex][ord(key[count]) - 97]
                else:
                    encryptedText += x
            print(encryptedText)
            input('Press ENTER to decrpyt.')
            decrypt(encryptedText, decryptedText)


        def decrypt(encryptedText, decryptedText):
            for count, x in enumerate(encryptedText):
                charIndex = ord(x.lower()) - 97
                if charIndex >= 0:
                    decryptedText += abc[vTable[ord(key[count]) - 97].index(x)]
                else:
                    decryptedText += x
            print(decryptedText)

        encrypt(encryptedText)

    vigenereTableGen()
    main()

def caesarCipher():
    # Collects the text that needs to be ciphered, the number of positions
    # the characters need to be shifted, and what method is to be used.
    shift = int(input('How many positions do you want to shift?\n'))
    while shift > 26:
            shift -= 26
    text = input('Enter what you what to cipher.\n')
    methodNum = 0
    while methodNum == 0:
        try:
            methodNum = int(input('Do you want to use method 1 or method 2?'
                ' (1 or 2)\n'))
            if (methodNum > 2) or (methodNum < 0):
                methodNum = 0
        except:
            print('Enter 1 or 2.')

    def method1():
        encryptedText = ''
        decryptedText = ''

        # Encryption
        for x in text:
            if not x == ' ':
                charIndex = ord(x.lower()) + shift - 97
                if charIndex > 24:
                    charIndex -= 26
                encryptedText += abc[charIndex]
            else:
                encryptedText += ' '
        print(encryptedText)
        input('Press ENTER to decrypt.')

        # Decryption
        for x in encryptedText:
            if not x == ' ':
                charIndex = ord(x) - shift - 97
                if charIndex < 0:
                    charIndex += 26
                decryptedText += abc[charIndex]
            else:
                decryptedText += ' '
        print(decryptedText)

    def method2():
        abcStr = ''
        shiftedStr = ''
        eText = ''
        dText = ''
        
        # Generates the alphabet and appends it to 'abcStr'.
        # Also generates 'shiftedStr'
        for x in range(26):
            abcStr += chr(97 + x)
            abcIndex = 97 + x + shift
            if abcIndex > 112:
                abcIndex -= 26
            shiftedStr += chr(abcIndex)

        # Encryption
        for x in text:
            if x.isspace():
                eText += x
            else:
                eText += shiftedStr[abcStr.find(x.lower())]
        print(eText)

        # Decryption
        input('Press ENTER to decrypt.')
        for x in eText:
            if x.isspace():
                dText += x
            else:
                dText += abcStr[shiftedStr.find(x.lower())]
        print(dText)

    if methodNum == 1:
        method1()
    else:
        method2()

# Caesars cipher but it divides the message into multiple pieces
# and moves the pieces around.
def caesarSliced():
    text = input('\nEnter a message to be ciphered.\n').lower()
    shift = int(input('\nHow many positions do you want to shift?\n'))
    encryptedText = ''
    decryptedText = ''

    def switcharoo(inputText):
        finalText = ''
        for i in range(2, 21):
            if (((len(inputText) % i) == 0)
                    and (len(inputText) <= (i * 4))
                    and not (i >= (len(inputText))) / 3):
                tempList = []
                front = 0
                back = 0
                for j in range(i):
                    back += int(len(inputText) / i)
                    tempList.append(inputText[front:back])
                    front += int(len(inputText) / i)
                for j in range(i):
                    if ((j % 2) == 0):
                        if ((i - j) < 2) and not ((i % 2) == 0):
                            finalText += tempList[j]
                        else:
                            finalText += tempList[j + 1]
                    else:
                        if (i - j) > 1:
                            finalText += tempList[j - 1]
                        else:
                            finalText += tempList[0]
                return finalText

    # Encryption
    for x in text:
        if not x == ' ':
            charIndex = ord(x.lower()) + shift - 97
            if charIndex > 24:
                charIndex -= 26
            encryptedText += abc[charIndex]
        else:
            encryptedText += ' '
    encryptedText = switcharoo(encryptedText)
    print(encryptedText)

    # Decryption
    input('\nPress ENTER to decrypt.\n')
    encryptedText = switcharoo(encryptedText)
    for x in encryptedText:
        if not x == ' ':
            charIndex = ord(x) - shift - 97
            if charIndex < 0:
                charIndex += 26
            decryptedText += abc[charIndex]
        else:
            decryptedText += ' '
    print(decryptedText)

# Generates the alpahabet and appends it to 'abc' list.
for x in range(26):
    abc.append(chr(97 + x))

# caesarCipher()
# vigenereCipher()
caesarSliced()