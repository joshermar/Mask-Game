#!/usr/bin/python3

from random import randint

def maskMaker(prefix):
	mask = [0,0,0,0]
	for i in range(len(mask)):
		if prefix > 8:
			mask[i] = 255
			prefix -= 8
			continue
		else:
			mask[i] = 256 - 2**(8-prefix)
			break
	return mask

while True:
	roundMask = maskMaker(randint(0,32))
	
	print("\n"*50)
	print('{}.{}.{}.{}'.format(roundMask[0],roundMask[1],roundMask[2],roundMask[3],))
	print('')

	answer = input("CIDR Prefix? ")
	
	if answer == str(roundPrefix):
		print()
		input('Righto! :)')
	else:
		print()
		input('Sorry! Try again :(')
