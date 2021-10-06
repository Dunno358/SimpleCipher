import os
def wrapper(text):
    text = str(text)
    text = text.upper()
    print("*************************************************{}***************************************************".format(text))   
def toCipher(text):
    charList = []
    ciphered = ""
    for x in str(text):
        charList.append(ord(x))
    for x in charList:
        cipheredChar = str(x) + "#"
        ciphered += cipheredChar
    ciphered = ciphered[:-1]
    return print("\nCiphering...\n\nCiphered Text(Unicode-1):\n" + ciphered+"\n")
def ceasearCipher(textin):
    ciphered = ""
    for char in textin:
        char = ord(char) + 1
        ciphered += chr(char)
    return print("\nCiphered text(Ceasear):\n" + ciphered+"\n")    
os.system(r"cls")    
wrapper("Enter text to cipher")
mainText = input(": ")
toCipher(mainText)
ceasearCipher(mainText)

os.system("pause")
os.system(r"C:\SimpleCipher\App\dist\SimpleCipher\SimpleCipher.exe")