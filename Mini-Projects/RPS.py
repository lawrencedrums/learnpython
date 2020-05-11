from random import randrange

comp_play = randrange(1, 3)
prompt = "What's your play? (1 for Rock, 2 for Paper, 3 for Scissors): "

while True:
    user_play = input(prompt)
    user_play = int(user_play)
    if (user_play < 1) or (user_play > 3):
        prompt = "Please enter 1 for Rock, 2 for Paper, 3 for Scissors: "
    else:
        break

if comp_play == 1:
    print("The computer played Rock!")
    if user_play == 1:
        print("It's a draw!")
    elif user_play == 2:
        print("You've won!")
    else:
        print("You've lost!")
elif comp_play == 2:
    print("The computer played Paper!")
    if user_play == 2:
        print("It's a draw!")
    elif user_play == 3:
        print("You've won!")
    else:
        print("You've lost!")
else:
    print("The computer played Scissors!")
    if user_play == 3:
        print("It's a draw!")
    elif user_play == 1:
        print("You've won!")
    else:
        print("You've lost!")            