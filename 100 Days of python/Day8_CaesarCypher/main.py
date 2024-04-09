
lowercase_letters = [chr(ord('a') + i) for i in range(26)]

def logo():
    pass

def cypher(inSentence, shiftKey, cypherType):
    i = 0
    for character in inSentence:
        if character.isalpha():
            if cypherType == "encode":
                asciiLetter = lowercase_letters[i+shiftKey]
            elif cypherType == "decode":
                asciiLetter = lowercase_letters[i-shiftKey]
            print(asciiLetter, end="")
            i = i + 1
        else:
            print(" ", end="")

if __name__ == "__main__":
    inSentence = input("Enter a sentence: ")
    shiftKey = int(input("Type the shift number: "))
    cypherType = input("Would you like to encode or decode?: ")
    cypher(inSentence = "hello world", shiftKey = 3, cypherType = "encode")