# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, config, compare



while config.player is False:
	# set config.player to True
	print("**********************************")
	print("Computer lives: ", config.computer_lives, "/",config.total_lives,"\n")
	print("Player lives: ", config.player_lives, "/",config.total_lives,"\n")
	print("Choose your weapon!\n")
	print("**********************************")

	config.player = input("choose rock, paper or scissors: ")
	config.player = config.player.lower()

	print("computer chose ", config.computer, "\n")
	print("player chose ", config.player, "\n")

	### this is where you would call compere

	### end compare stuff
	compare.comparechoices(config.computer, config.player)

	# handle all lives lost for config.player or AI
	if config.player_lives is 0:
		winlose.winorlose("lost")

	elif config.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		config.player = False
		config.computer = config.choices[randint(0, 2)]