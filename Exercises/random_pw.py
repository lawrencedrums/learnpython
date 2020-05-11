import string, random

def gen_password(length, number, symbol=0):
	"""Generate a random password with user's specification."""
	password = []
	length = length - number
	for i in range(0, length):
		password.append(random.choice(string.ascii_letters))
	for i in range(0, number):
		password.append(random.choice(string.digits))
	random.shuffle(password)
	joined_password = "".join(password)
	print(f"\n{joined_password}")
		
while True:
	length = input("Please enter the length of password: ")
	try:
		length = int(length)
		if length < 6 or length > 32:
			print("Your password must be between 6 and 32 digits long.")
			continue
		else:
			break
	except ValueError:
		print("Please enter a number!")
	else:
		break

while True:
	number = input("\nHow many numbers would you like to have in your password? ")
	try:
		number = int(number)
		if number >= length or number < 1:
			print(f"Please enter a value between 1 and {length-1}!")
			continue
		else:
			break
	except ValueError:
		print("Please enter a number!")
		
gen_password(length, number)
