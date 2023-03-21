import random
import sys

life_count = 6
display = []
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

for _ in chosen_word:
    display += "_"
word_list = list(str(chosen_word))

# * V3 of While function, added game win and lose condition
while life_count != 0:
    if "_" not in display:
        print("You win.")
        sys.exit()
    elif "_" in display:
        guess = str.lower(input("Guess a letter\n"))
        if guess not in chosen_word:
            life_count -= 1
            print("Wrong")
            if life_count > 1:
                print(f"You have {life_count} guesses left.")
            elif life_count == 0:
                print("You've ran out of guesses, you lose.")
                sys.exit()
            else:
                print(f"You have {life_count} guess left.")
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
