import random
from hangman_art import logo, stages
# ^ Can import parts of a file separatly 
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#logo
print(logo)

#Blanks
display = []
for _ in range(word_length):
    display += "_"

#Game itself 
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    #Converting list elements to string 
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #stage image
    print(stages[lives])