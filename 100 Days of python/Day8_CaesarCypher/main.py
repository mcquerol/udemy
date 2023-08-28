# inPhrase = input("Enter a sentence: ")
# key = int(input("what is the key: "))

# for x in inPhrase:
#     asciiNum = ord(x)
#     asciiNum+= key
#     asciiLetter = chr(asciiNum)
#     print(asciiLetter, end="")
lowercase_letters = [chr(ord('a') + i) for i in range(26)]

def logo():
    pass

def cypher(inSentence, shiftKey, cypherType):
    i = 0
    for character in inSentence:
        # if cypherType == "encode":
        #     asciiLetter = lowercase_letters[i+shiftKey]
        # elif cypherType == "decode":
        #     asciiLetter = lowercase_letters[i-shiftKey]
        if character.isalpha():
            print(character, end="")
        else:
            print(" ", end="")
    #print(asciiLetter, end="")

if __name__ == "__main__":
    #inSentence = input("Enter a sentence: ")
    #shiftKey = int(input("Type the shift number: "))
    #cypherType = input("Would you like to encode or decode?: ")
    cypher(inSentence = "hello world", shiftKey = 3, cypherType = "decode")