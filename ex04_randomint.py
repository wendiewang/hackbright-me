#!usr/bin/python 

#greet player
#    get player name
#    choose random number between 1 and 100
#   while True:
#       get guess
#      if guess is incorrect:
#           give hint
#       else:
#           congratulate player

import random 

print "greetings player! what is your name?" 
name = raw_input("> ")
print "hi %r, lets play a game! i have a secret number between 1 - 100, guess what my number is?" %(name)

secret_number = random.randint(1,100) 

while True: 
	guess = int(raw_input("> ")) 
	if guess > secret_number:
		print "too high"
	elif guess < secret_number:
		print "too low"
	else: 
		print "congrats! you won"
		break 

