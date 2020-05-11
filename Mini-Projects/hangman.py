import random

words = {'water': 'it flows', 
		'knight': 'a noble', 
		'recycle': 'good for the earth', 
		'jewelery': 'precious items', 
		'november': '11',
		'espresso': 'black and strong'}

life = 7
the_word = []
guesses = []
check = []

#Get a random word and the hint from the dictionary
random_word, hint = random.choice(list(words.items()))
#Storing each letter of the word in a list
for c in random_word:
	the_word.append(c)

while life > 0:
	check = []
	for c in the_word:
		if c not in guesses:
			print("_", end=" ")
		else:
			print(c, end=" ")
			check.append(c)
	if sorted(check) == sorted(the_word):
		print("\nYou've won! Congratulations!")
		break
	print(f"\nYou have {life} lifes left.")
	guess = input("Guess a letter: ")
	if guess not in the_word:
		life = life - 1
	else:
		guesses.append(guess)
	print('\n')
	if life == 3:
		print(f"Here's a hint... '{hint.title()}'")
else:
	print(f"You've died!\nThe answer is {the_word}.")