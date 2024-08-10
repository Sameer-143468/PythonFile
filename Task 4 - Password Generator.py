import string
import random

length = int(input("Enter Password Length: "))
print('''Enter Choice : 
		1. Letters
		2. Digits
		3. Special characters
		4. Exit''')

characterList = ""

while(True):
	choice = int(input("Enter the Choice: "))
	if(choice == 1):
		characterList += string.ascii_letters
	elif(choice == 2):
		characterList += string.digits
	elif(choice == 3):
		characterList += string.punctuation
	elif(choice == 4):	
		break
	else:
		print("In-Valid Choice...!")

password = []

for i in range(length):
	randomchar = random.choice(characterList)
	password.append(randomchar)
	
print("The Strong Password is: " + "".join(password))
