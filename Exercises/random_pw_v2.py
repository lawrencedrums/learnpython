import string, random, math

def gen_password(length, number, symbol=0):
	"""Generate a random password with user's specification."""
	password = []
	symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
	length = length - number - symbol
	for i in range(0, length):
		password.append(random.choice(string.ascii_letters))
	for i in range(0, number):
		password.append(random.choice(string.digits))
	for i in range(0, symbol):
		password.append(random.choice(symbols))
	random.shuffle(password)
	joined_password = "".join(password)
	print(f"\n{joined_password}")
		
while True:
	length = input("Please enter the length of password: ")
	try:
		length = int(length)
		if length < 8 or length > 40:
			print("Your password must be between 8 and 40 digits long.")
			continue
		else:
			break
	except ValueError:
		print("Please enter a number bewteen 8 and 40.")
	else:
		break

number_boolean = input("\nInclude numbers? (Y/N): ")
while True:
	if number_boolean.upper() == 'Y':
		number = input("How many numbers? ")
		try:
			number = int(number)
			if number > length/2 or number < 1:
				print(f"Please enter a number between 1 and {math.floor(length/2)} !")
				continue
			else:
				break
		except ValueError:
			print(f"Please enter a number between 1 and {math.floor(length/2)}!")
	elif number_boolean.upper() == 'N':
		number = 0
		break
	else:
		print("Please only enter Y or N.")
		number_boolean = input("\nInclude numbers? (Y/N): ")
		continue
		
symbol_boolean = input("\nInclude symbols? (Y/N): ")
while True:
	if symbol_boolean.upper() == 'Y':
		symbol = input("How many symbols? ")
		try:
			symbol = int(symbol)
			if symbol > math.floor(length/2) or symbol < 1:
				print(f"Please enter a number between 1 and {math.floor(length/2)} !")
				continue
			else:
				break
		except ValueError:
			print(f"Please enter a number between 1 and {math.floor(length/2)}!")
	elif symbol_boolean.upper() == 'N':
		symbol = 0
		break
	else:
		print("Please only enter Y or N.")
		symbol_boolean = input("\nInclude symbols? (Y/N): ")
		continue
					
gen_password(length, number, symbol)
