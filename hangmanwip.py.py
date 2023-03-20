import sys
life_count = 6
display = []
word_list = ["aardvark", "baboon", "camel"]

import random
chosen_word = random.choice(word_list)
print(chosen_word)

for _ in chosen_word:
    display += "_"
word_list = list(str(chosen_word))
while life_count !=0: #or "_" not in display:
  if "_" not in display:
    print("You win.")
    sys.exit()
  elif "_" in display:
    guess = str.lower(input("Guess a letter\n"))
    for position in range(len(chosen_word)):
      letter = chosen_word[position] 
      if guess == letter:
        display[position] = guess
        
  else:
    if guess not in chosen_word:
        life_count-=1
        print(life_count)
        print("Wrong")
    
        
  print(display)
   # This code is looping the amount of times as the number of letters in the chosen word list, and saving that number. Which then gets assigned as the index value in the chosen_word list for letter variable. Then the if statement then uses that indexed value and checks it against the user's guess. If it matches it will then take that same position variable to change the item in the display list for the user to see.
if life_count == 0:
  print("You lose.")





  
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

  
