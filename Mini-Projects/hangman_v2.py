import random

words = ['aubergine', 'breakfast', 'calender', 
        'dilemma', 'essential', 'fabric']

answer = random.choice(list(words))
guesses = []
wrong_guesses = []
life = 5

while life > 0:
    i = 0
    check_answer = []
    for letter in answer:
        if answer[i] in guesses:
            print(answer[i], end=" ")
            check_answer.append(answer[i])
            if ''.join(check_answer) == answer:
                print("Congratulations! You've won!")
                break
        else:
            print("_", end=" ")
        i += 1
    guess = input("\nTake a guess: ")
    if guess not in answer:
        life -= 1
        wrong_guesses.append(guess)
    else:
        guesses.append(guess)
    print(f"Your wrong aguesses: ", end="")
    print(*wrong_guesses, sep=", ")
    print(f"You have {life} lifes left.\n")
else:
    print(f"You have lost! The answer is {answer}")