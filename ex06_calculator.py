# No setup
# repeat forever:
# read input
# tokenize input
# if the first token is 'q', quit
# otherwise decide which math function to call based on the tokens we read

import arithmetic

while True: 
	calculate = raw_input('> ')
	calculate = calculate.split(" ")
	#.split tokenizes so then u can use [0] to reference a spot 
	if calculate[0] == 'q':
		break
	else:
		if calculate[0] == '+':
			print arithmetic.add(int(calculate[1]), int(calculate[2]))
		elif calculate[0] == '-': 
			print arithmetic.subtract(int(calculate[1]), int(calculate[2]))
		elif calculate[0] == '*':
			print arithmetic.multiply(int(calculate[1]), int(calculate[2]))
		elif calculate[0] == '/':
			print arithmetic.divide(int(calculate[1]), int(calculate[2]))
		elif calculate[0] == 'square':
			print arithmetic.square(int(calculate[1]))
		elif calculate[0] == 'cube':
			print arithmetic.cube(int(calculate[1]))
		elif calculate[0] == 'pow':
			print arithmetic.power(int(calculate[1]), int(calculate[2]))
		elif calculate[0] == 'mod':
			print arithmetic.mod(int(calculate[1]), int(calculate[2]))
		else:
			"you typed it in wrong!"
	
