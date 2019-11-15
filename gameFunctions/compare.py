from gameFunctions import config


#what you trying to compare inside this function?
#you will need to pass those things in as arguments
#inside the round brackets

def comparechoices(cmpt, plr):
	if plr == "quit":
		exit()
	elif cmpt == plr:
		print("tie! no one wins, play again")

	elif plr == "rock":
		if cmpt == "paper":
			print("You lose!", cmpt, "covers", plr, "\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", plr, "smashes", cmpt, "\n")
			config.computer_lives = config.computer_lives - 1

	elif plr == "paper":
		if cmpt == "scissors":
			print("You lose!", cmpt,"cuts", config.player, "\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", plr, "covers", cmpt, "\n")
			config.computer_lives = config.computer_lives - 1

	elif plr == "scissors":
		if cmpt == "rock":
			print("You lose!", cmpt, "smashes", plr, "\n")
			config.player_lives = config.player_lives - 1
		else:
			print("You win!", plr, "cuts", cmpt, "\n")
			config.computer_lives = config.computer_lives - 1

	else:
		print("That's not a valid choice, try again")