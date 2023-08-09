import random as rand;
word_list = ["aardvark", "baboon", "camel"]

#Step 1 -- get random word from sample word list and get a user input (letter) then check if it is in the word
# import random as rand;
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = rand.choice(word_list)
# guess = input("Guess a letter: ").lower()
# for letter in chosen_word:
#     if letter == guess:
#         print("yes") #letter guessed is in the word
#     else:
#         print("no") #letter guessed is not in the word


#Step 2 -- create blank array and if the letter guessed is part of the word then fill it in
# display = []
# word_length = len(chosen_word)
# for _ in range(word_length):
#     display += "_"
    
# for position in range(word_length):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter


#Step 3 -- create main loop and checks for win condition
win = False
chosen_word = rand.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not win:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        win = True
        print("You win!")