import pygame


def print_letter(window, letter, position, thickness, size, color):

	letters = {"A":[(position[0]+(size/8),position[1]+size),(position[0] + size/2,position[1]+0),(position[0] + (7*size/8),position[1]+size),(position[0] + (5*size/8),position[1]+(size/2)),( position[0]+(3*size/8), position[1]+size/2)],
		"B":[(position[0]+(size/8), position[1]+size), (position[0]+(size/8),position[1]),(position[0]+(size/8)+(5*size/8),position[1]),(position[0]+(size/8)+(7*size/8),position[1]+(1*size/8)),(position[0]+(size/8)+(7*size/8),position[1]+(2*size/8)),(position[0]+(size/8)+(5*size/8),position[1]+(3*size/8)),(position[0]+(size/8)+(7*size/8),position[1]+(4*size/8)),(position[0]+(size),position[1]+(7*size/8)),(position[0]+(7*size/8),position[1]+(size)),(position[0]+(size/8),position[1]+(size)) ],
		"C":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(3*size/8), position[1]),(position[0]+(1*size/8), position[1]+(3*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(3*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)), ],
		"D":[(position[0]+(size/8), position[1]+size), (position[0]+(size/8),position[1]), (position[0]+(5*size/8),position[1]), (position[0]+(7*size/8),position[1]+(2*size/8)), (position[0]+(7*size/8),position[1]+(6*size/8)), (position[0]+(5*size/8),position[1]+(size)),(position[0]+(size/8), position[1]+size) ],
		"E":[(position[0]+(7*size/8), position[1]), (position[0]+(size/8),position[1]), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(6*size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(size)), (position[0]+(7*size/8),position[1]+(size)) ],
		"F":[(position[0]+(7*size/8), position[1]), (position[0]+(size/8),position[1]), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(6*size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(4*size/8)), (position[0]+(size/8),position[1]+(size)) ],
		"G":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(3*size/8), position[1]),(position[0]+(1*size/8), position[1]+(3*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(3*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(7*size/8), position[1]+(5*size/8)),(position[0]+(5*size/8), position[1]+(5*size/8)) ],
		"H":[(position[0]+(size/8), position[1]),(position[0]+(size/8), position[1]+size/2),(position[0]+(7*size/8), position[1]+size/2),(position[0]+(7*size/8), position[1]),(position[0]+(7*size/8), position[1]+size),(position[0]+(7*size/8), position[1]+size/2),(position[0]+(size/8), position[1]+size/2),(position[0]+(size/8), position[1]+size)],
		"I":[(position[0]+(2*size/8), position[1]),(position[0]+(6*size/8), position[1]),(position[0]+(size/2), position[1]),(position[0]+(size/2), position[1]+(size)),(position[0]+(1*size/8), position[1]+size),(position[0]+(7*size/8), position[1]+size),],
		"J":[(position[0]+(size/8), position[1]),(position[0]+(7*size/8), position[1]),(position[0]+(7*size/8), position[1]+(5*size/8)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(7*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),],
		"K":[(position[0]+(size/8), position[1]),(position[0]+(size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]),(position[0]+(size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(4*size/8)),(position[0]+(size/8), position[1]+(size))],
		"L":[(position[0]+(size/8), position[1]),(position[0]+(size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(size))],
		"M":[(position[0]+(size/8), position[1]+(size)),(position[0]+(size/8), position[1]),(position[0]+(4*size/8), position[1]+(size/3)),(position[0]+(7*size/8), position[1]),(position[0]+(7*size/8), position[1]+(size))],
		"N":[(position[0]+(size/8), position[1]+(size)),(position[0]+(size/8), position[1]),(position[0]+(7*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1])],
		"O":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(1*size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)), (position[0]+(7*size/8), position[1]+(2*size/8))],
		"P":[(position[0]+(size/8), position[1]+(size)),(position[0]+(size/8), position[1]),(position[0]+(5*size/8), position[1]),(position[0]+(7*size/8), position[1]+(1*size/8)),(position[0]+(7*size/8), position[1]+(4*size/8)),(position[0]+(5*size/8), position[1]+(5*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),],
		"Q":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(1*size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(5*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(size)),(position[0]+(5*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(5*size/8)), (position[0]+(7*size/8), position[1]+(2*size/8))],
		"R":[(position[0]+(size/8), position[1]+(size)),(position[0]+(size/8), position[1]),(position[0]+(5*size/8), position[1]),(position[0]+(7*size/8), position[1]+(1*size/8)),(position[0]+(7*size/8), position[1]+(4*size/8)),(position[0]+(5*size/8), position[1]+(5*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(7*size/8), position[1]+(size))],
		"S":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(5*size/8), position[1]),(position[0]+(3*size/8), position[1]),(position[0]+(size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(5*size/8), position[1]+(size)),(position[0]+(3*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(6*size/8))],
		"T":[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(4*size/8), position[1]),(position[0]+(7*size/8), position[1]),(position[0]+(size/8), position[1]),],
		"U":[(position[0]+(size/8), position[1]),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(7*size/8), position[1])],
		"V":[(position[0]+(size/8), position[1]),(position[0]+(4*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1])],
		"W":[(position[0]+(size/8), position[1]),(position[0]+(2*size/8), position[1]+size),(position[0]+(4*size/8), position[1]+(4*size/8)),(position[0]+(4*size/8), position[1]+(4*size/8)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1])],
		"X":[(position[0]+(size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]),(position[0]+(4*size/8), position[1]+(4*size/8)),(position[0]+(size/8), position[1]),(position[0]+(7*size/8), position[1]+(size))],
		"Y":[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(4*size/8), position[1]+(4*size/8)),(position[0]+(size/8), position[1]),(position[0]+(4*size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1])],
		"Z":[(position[0]+(size/8), position[1]),(position[0]+(7*size/8), position[1]),(position[0]+(size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(size))],
		"0":[(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(size/8), position[1]+(2*size/8)),(position[0]+(2*size/8), position[1]),(position[0]+(6*size/8), position[1]),(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(7*size/8), position[1]+(2*size/8)),],
		"1":[(position[0]+(size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(size)),(position[0]+(4*size/8), position[1]+(size)),(position[0]+(4*size/8), position[1]),(position[0]+(2*size/8), position[1]+(4*size/8))],
		"2":[(position[0]+(7*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(3*size/8)),(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(size/8), position[1]+(2*size/8))],
		"3":[(position[0]+(size/8), position[1]+(2*size/8)),(position[0]+(2*size/8), position[1]),(position[0]+(6*size/8), position[1]),(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(7*size/8), position[1]+(3*size/8)),(position[0]+(5*size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(6*size/8)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(6*size/8))],
		"4":[(position[0]+(6*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(7*size/8), position[1]+(6*size/8))],
		"5":[(position[0]+(7*size/8), position[1]),(position[0]+(size/8), position[1]),(position[0]+(size/8), position[1]+(4*size/8)),(position[0]+(2*size/8), position[1]+(3*size/8)),(position[0]+(6*size/8), position[1]+(3*size/8)),(position[0]+(7*size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(7*size/8)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(size/8), position[1]+(7*size/8))],
		"6":[(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(6*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(7*size/8)),(position[0]+(7*size/8), position[1]+(5*size/8)),(position[0]+(6*size/8), position[1]+(4*size/8)),(position[0]+(size/8), position[1]+(4*size/8))],
		"7":[(position[0]+(size/8), position[1]),(position[0]+(7*size/8), position[1]),(position[0]+(3*size/8), position[1]+(6*size/8)),(position[0]+(3*size/8), position[1]+(size))],
		"8":[(position[0]+(2*size/8), position[1]),(position[0]+(6*size/8), position[1]),(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(size/8), position[1]+(5*size/8)),(position[0]+(size/8), position[1]+(7*size/8)),(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(7*size/8)),(position[0]+(7*size/8), position[1]+(5*size/8)),(position[0]+(size/8), position[1]+(2*size/8)),(position[0]+(2*size/8), position[1])],
		"9":[(position[0]+(2*size/8), position[1]+(size)),(position[0]+(6*size/8), position[1]+(size)),(position[0]+(7*size/8), position[1]+(7*size/8)),(position[0]+(7*size/8), position[1]+(2*size/8)),(position[0]+(6*size/8), position[1]),(position[0]+(2*size/8), position[1]),(position[0]+(size/8), position[1]+(1*size/8)),(position[0]+(size/8), position[1]+(3*size/8)),(position[0]+(2*size/8), position[1]+(4*size/8)),(position[0]+(7*size/8), position[1]+(4*size/8))],
	}
	
	pygame.draw.aalines(window,color, False, letters[letter], thickness)

def print_symbol(window, symbol, position, thickness, size, color):
	symbols = {
		"!":[[(position[0]+(4*size/8), position[1]),(position[0]+(4*size/8), position[1]+(6*size/8))],[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(11*size/20), position[1]+(size)),(position[0]+(9*size/20), position[1]+(size)),] ],
		":":[[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(11*size/20), position[1]+(size)),(position[0]+(9*size/20), position[1]+(size)),] ,[(position[0]+(11*size/20), position[1]+(size/2)),(position[0]+(9*size/20), position[1]+(size/2)),(position[0]+(4*size/8), position[1]+(size/2)),] ],
		"?":[],
		".":[[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(11*size/20), position[1]+(size)),(position[0]+(9*size/20), position[1]+(size)),]],
		",":[[(position[0]+(4*size/8), position[1]+(size)),(position[0]+(size/2), position[1]+(10*size/8)),(position[0]+(size/2), position[1]+(size)),]],
	}
		
	if symbol != " ":
		for i in range(len(symbols[symbol])):
			pygame.draw.aalines(window,color, False, symbols[symbol][i], thickness)
		

def print_text(window, text, position, thickness, size, color):
	space = size/8
	symbolstr = "!:? .,"
	for idx, letter in enumerate(text):
		if letter in symbolstr:
			print_symbol(window, letter, (position[0]+idx*(size+space),position[1]),thickness,size, color)
		else:
			print_letter(window, letter.upper(), (position[0]+idx*(size+space),position[1]),thickness,size, color)
