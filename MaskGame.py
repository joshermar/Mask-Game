#!/usr/bin/python3

from random import randint

subnetMasks = [
				[0,0,0,0],
				[128,0,0,0],
				[192,0,0,0],
				[224,0,0,0],
				[240,0,0,0],
				[248,0,0,0],
				[252,0,0,0],
				[254,0,0,0],
				[255,0,0,0],
				[255,128,0,0],
				[255,192,0,0],
				[255,224,0,0],
				[255,240,0,0],
				[255,248,0,0],
				[255,252,0,0],
				[255,254,0,0],
				[255,255,0,0],
				[255,255,128,0],
				[255,255,192,0],
				[255,255,224,0],
				[255,255,240,0],
				[255,255,248,0],
				[255,255,252,0],
				[255,255,254,0],
				[255,255,255,0],
				[255,255,255,128],
				[255,255,255,192],
				[255,255,255,224],
				[255,255,255,240],
				[255,255,255,248],
				[255,255,255,252],
				[255,255,255,254],
			  ]

def countOnes(number):
	ones = 0
	while number > 0:
		if number % 2:
			ones += 1
		number //= 2
	return ones

while True:
	currentMask = subnetMasks[randint(0,31)]
	currentCount = 0+countOnes(currentMask[0])+countOnes(currentMask[1])+countOnes(currentMask[2])+countOnes(currentMask[3])
	
	print(
		"\n"+
		"\n"+
		"\n"+
		"\n"+
		"\n"+
		str(currentMask[0])+"."+str(currentMask[1])+"."+str(currentMask[2])+"."+str(currentMask[3])
		)
	
	answer = input("CIDR Prefix? ")
	
	if answer == str(currentCount):
		print(
			"\n"+
			str(answer)+" is "+"Right! :)"
			)
	else:
		print(
			"\n"+
			str(answer)+" is "+"Wrong :("
			)
