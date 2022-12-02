abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def vigenereCipher():
    vTable = []

    def vigenereTableGen():
        for count, i in enumerate(abc):
            tempList = []
            for j in abc:
                charIndex = ord(abc[ord(j) - 97])
                if charIndex + count > 122:
                    charIndex -= 26
                tempList.append(chr(charIndex + count))
            vTable.append(tempList)

    def keyLength(text, key):
        if not len(text) == len(key):
            for x in range(len(text) - len(key)):
                if x > len(key):
                    x -= len(key)
                key += key[x]
        return key

    def main():
        encryptedText = ''
        key = ' '
        text = input('Enter what you want to cipher.\n')
        while ' ' in key:
            key = keyLength(text, input('Enter a keyword (no spaces).\n'))
        for count, x in enumerate(text):
            charIndex = ord(x.lower())
            if charIndex > 90:
                encryptedText += vTable[charIndex - 97][ord(key[count]) - 97]
            else:
                encryptedText += x
        print(encryptedText)

    vigenereTableGen()
    main()

def caesarCipher():
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

caesarCipher()
# vigenereCipher()