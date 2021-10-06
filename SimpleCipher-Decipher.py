import os
def wrapper(text):
    text = str(text)
    text = text.upper()
    print("************************************************{}**************************************************".format(text))
def toDecipher(text):
    deciphered = ""
    decipherChars = text.split("#")
    for x in decipherChars:
        deciphered += chr(int(x))
    return print("\nDeciphering...\n\nDeciphered Text:\n" + deciphered)
def ceasearDecipher(textin):
    deciphered = ""
    for char in textin:
        char = ord(char) - 1
        deciphered += chr(char)
    return print("Deciphered text:\n" + deciphered)
os.system(r"cls")
action = input("Choose ciphering type:\nUnicode - 1\nCeasear - 2\n: ")
wrapper("Enter text to decipher")
mainText = input(": ")
if action == "1":
    try:
        toDecipher(mainText)
    except ValueError:
        print("\nText must be ciphered correctly!")
elif action == "2":
    ceasearDecipher(mainText)
else:
    print("Incorrect type!")
programEnd = input("\nPress enter to end...")
if programEnd == "":
    os.system(r"cls")
    os.system(r"C:\SimpleCipher\Data\dist\SimpleCipher\SimpleCipher.exe") 