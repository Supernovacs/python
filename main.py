def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        elif (char == " "):
            result += " "
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result

print("Enter the text you want to encode: ")
text = input()
print("Enter the key: ")
s = int(input())
print("Here's your secret message: " + encrypt(text,s))