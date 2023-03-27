# Write your code below this line 👇
def prime_checker(number):
    no_prime_list = ["0", "2", "4", "6", "8"]
# Turns the user input's number into a list that contains each digit of the number
    numbers = list(str(number))
    numbers_int = list(map(int, numbers))
    print(sum(numbers_int))
# Adds up all the digits of the numbers list
    if numbers[-1] in no_prime_list:
        print("It's not a prime number.")
    elif sum(numbers_int) % 3 == 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
