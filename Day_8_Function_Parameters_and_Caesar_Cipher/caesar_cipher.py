#Letter database in which the caesar function will be pulling from
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#Asks input questions to get the arguments for caesar function
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#* Caesar Function
def caesar(text, shift, direction):
#Encryption
    if direction == "encode":
        cipher = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25:
                # This code prevents the glitching of if the input extends beyond the original alphabet list, if it does, it creates a new list that doubles the original one,
                # essentially making it repeat, if it doesn't go over however, it continues the decryption within the original list
                extended_alphabet = alphabet + alphabet
                position = extended_alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = extended_alphabet[new_position]
                cipher += new_letter
            else:
                new_letter = alphabet[new_position]
                cipher += new_letter
        print(f"The encoded text is {cipher}")
#Decryption
    elif direction == "decode":
        d_cipher = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            d_cipher += new_letter
        print(f"The decoded text is {d_cipher}")
    else:
        print("Invalid direction.")

caesar(text, shift, direction)