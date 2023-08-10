import random as rand
import art
import words

isGameOver = False
chosen_word = rand.choice(words.word_list)
word_length = len(chosen_word)
print(art.logo)
display = []
for _ in range(word_length):
    display += "_"

lives = len(art.stages)-1

lettersGuessed = [] #array of letters already guessed

while not isGameOver:
    guess = input("Guess a letter: ").lower()
    if guess in lettersGuessed:
        print(f"You alreday guessed letter {guess}..try again ")
        continue
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            lettersGuessed += letter
    print(f"{' '.join(display)}")


    if guess not in chosen_word:
        lives -=1

    if "_" not in display:
        isGameOver = True
        print("You win!")
    if lives == 0:
        isGameOver = True
        print("You lose!")
    print(art.stages[lives])