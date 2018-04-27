#!/usr/bin/python3

from random import randint

def maskMaker(prefix):
	mask = [0,0,0,0]
	for i in range(len(mask)):
		# We have to separate the prefix into octets
		if prefix > 8:
			mask[i] = 255
			prefix -= 8
		else:
			mask[i] = 256 - 2**(8-prefix)
			break
	return mask


mode = 0

while not mode:
	print('Select one of the following options:')
	print('')
	print('m - Mask (you will be prompted for a prefix)')
	print('p - Prefix (you will be prompted for a mask)')
	print('r - Random')
	print('')
	print('You can enter \'q\' at any time to quit')
	
	modeAnswer = input('')
	
	if modeAnswer == 'q' or modeAnswer == 'Q':
		break
	elif modeAnswer == 'm' or modeAnswer == 'M':
		mode = 1
	elif modeAnswer == 'p' or modeAnswer == 'P':
		mode = 2
	elif modeAnswer == 'r' or modeAnswer == 'R':
		mode = 3

while mode:
	prefix = randint(0,32)

	maskList = maskMaker(prefix)

	maskString = '{}.{}.{}.{}'.format(maskList[0],maskList[1],maskList[2],maskList[3],)

	if mode == 3:
		roundMode = randint(1,2)
	else:
		roundMode = mode

	if roundMode == 2:
		question = '/' + str(prefix)
		questionPrompt = 'Subnet mask: '
		answer = maskString
	else:
		question = maskString
		questionPrompt = 'CIDR prefix: '
		answer = str(prefix)

	print("\n"*50)
	print(question)
	print('')

	response = input(questionPrompt)
	# Check response for 'q'
	if response == 'q' or response == 'Q':
		break

	if response == answer:
		print('')
		response = input('Righto! :) ')
	else:
		print('')
		response = input('Sorry! Try again :( ')
	# Check if q was entered after the question was answered
	if response == 'q' or response == 'Q':
		break
