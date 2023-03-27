import random
import sys
import hangman_words
import hangman_art

print(hangman_art.logo)
life_count = 6
display = []
chosen_word = random.choice(hangman_words.word_list)

for _ in chosen_word:
    display += "_"
word_list = list(str(chosen_word))
print(display)
# * V3 of While function, added game win and lose condition
while life_count != 0:
    if "_" not in display:
        print("You win.")
        sys.exit()
    elif "_" in display:
        guess = str.lower(input("Guess a letter\n"))
        if guess not in chosen_word:
            life_count -= 1
            print(f"{guess} is not in the word.")
            print(hangman_art.stages[life_count])
            if life_count > 1:
                print(f"You have {life_count} guesses left.")
            elif life_count == 0:
                print(f"The word was {chosen_word} ")
                print("You've ran out of guesses, you lose.")
                sys.exit()
            else:
                print(f"You have {life_count} guess left.")
        # Tells the player they've already guessed the letter
        else:
            if guess in display:
                print("You've already guessed that letter")
            else:
                for position in range(len(chosen_word)):
                    letter = chosen_word[position]
                    if guess == letter:
                        display[position] = guess

    print(display)


#! Failed Code Previously tried
# display_list = word_list.copy()
# change_counter = 0
# for i in display_list:
#   display_list[change_counter] = "_"
#   change_counter+=1
# print(display_list)

# for i in word_list:
#   if guess == i:
#     display_index = word_list.index(i)
#     display_list[display_index] = guess
#     print(display_list)
#   else:
#     #Add code here for when user guesses wrong
#     print("Incorect")
