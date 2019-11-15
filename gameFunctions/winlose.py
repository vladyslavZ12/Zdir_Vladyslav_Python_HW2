from random import randint
from gameFunctions import config
# define a python function that takes an argument
def winorlose(status): 
	# status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")

	print("You", status + "! Would you like to play again?")
	print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")

	choice = input("Y / N: ")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
		print("You chose to quit.")
		print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
		exit()

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		# this will break, currently - we will fix this next class
		
		
		config.player_lives = 5
		config.computer_lives = 5
		config.total_lives = 5
		config.player = False
		config.computer = config.choices[randint(0,2)]
	
	else:
		# not a y or n, so make the user pick a valid choice
		#!!!print("make a valid choice, Y or N")
		# this is recursion - call a function
		# from inside itself. Basically just re-up the choice
		# and force the user to pick yes or no (y or n)
		# 
		# use recursion until we get the right input
		# recursion is just a fancy way to describe calling a function from withon itself
		winorlose(status)