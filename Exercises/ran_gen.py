from random import randrange

def guess_number(small_num, big_num):
    """Prompt the user to input a number between 1 and 20."""
    guess = input(f"Guess a number between {small_num}-{big_num}. ")
    return int(guess)

random_number = randrange(1, 20)

small_num = 1
big_num = 20

while True:
    guess = guess_number(small_num, big_num)
    if guess > big_num or guess < small_num:
    	print("Your guess is invalid!")
    elif guess > random_number:
        print(f"The number is smaller than {guess}! ")
        big_num = guess
    elif guess < random_number:
        print(f"The number is bigger than {guess}! ")
        small_num = guess
    else:
        print(f"{guess} is correct!")
        break
