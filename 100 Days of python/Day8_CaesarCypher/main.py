# inPhrase = input("Enter a sentence: ")
# key = int(input("what is the key: "))

# for x in inPhrase:
#     asciiNum = ord(x)
#     asciiNum+= key
#     asciiLetter = chr(asciiNum)
#     print(asciiLetter, end="")

def logo():
    pass

def cypher(inSentence, shiftKey, cypherType):
    for character in inSentence:
        asciiNum = ord(character)
        if cypherType == "encode":
            asciiNum+= shiftKey
        elif cypherType == "decode":
            asciiNum-= shiftKey
        asciiLetter = chr(asciiNum)
        print(asciiLetter, end="")
            

if __name__ == "__main__":
    inSentence = input("Enter a sentence: ")
    shiftKey = int(input("Type the shift number: "))
    cypherType = input("Would you like to encode or decode?:")
    cypher(inSentence, shiftKey, cypherType)