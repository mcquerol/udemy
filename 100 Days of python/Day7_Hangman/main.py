#Step 1 
import random as rand;

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
randIndex = rand.randint(0,len(word_list)-1)
chosen_word = word_list[randIndex]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for x in chosen_word:
    if x == guess:
        print("yes") #letter guessed is in the word
    else:
        print("no") #letter guessed is not in the word