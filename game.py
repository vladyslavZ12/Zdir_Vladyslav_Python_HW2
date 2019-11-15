# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, config, compare



while config.player is False:
	# set config.player to True
	print("■■■■■■■■□□□ Rock Paper Scissors □□□■■■■■■■■")
	print("♡ ♡ ♡ ♡ ♡ Computer lives ♡ ♡ ♡ ♡ ♡ :", config.computer_lives, "/",config.total_lives,)
	print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ")
	print("♡ ♡ ♡ ♡ ♡ Player lives ♡ ♡ ♡ ♡ ♡ : ", config.player_lives, "/",config.total_lives,)
	print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ")
	print("↣↣↣↣↣↣↣↣↣Choose your weapon↣↣↣↣↣↣↣↣↣!")
	print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ")

	

	config.player = input("choose rock, paper or scissors: ")
	config.player = config.player.lower()

	print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬computer chose▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ", config.computer,)
	print("●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬player chose▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● ", config.player, )

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