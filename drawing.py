import sys
import shutil
import utils
import variables

def draw():
	clear()
	buildFrame()
	cursorTo(variables.pos_x, variables.pos_y, True)
	utils.doPrint('A')
	sys.stdout.flush()

def buildFrame():
	cursorTo(0, variables.height+1, True)
	utils.doPrint(utils.build('_', variables.width))
	for i in range(0, variables.height + 1):
		cursorTo(variables.width + 1, i, True)
		utils.doPrint('|')
	sys.stdout.flush()

def cursorTo(x, y, gameCoords):
	if gameCoords:
		gameY = shutil.get_terminal_size((80, 20))[1] - y
		print("\033[" + str(gameY) + ";" +  str(x) + "H", end='')
	else:
		print("\033[" + str(y) + ";" +  str(x) + "H", end='')



def clearAll():
	windowSize = shutil.get_terminal_size((80, 20))
	cursorTo(0, 0, False)
	for i in range(0, windowSize[1]):
		print(utils.build(' ', windowSize[0]), end='')
		if i is not variables.height:
			print('')

def clear():
	global height
	windowSize = shutil.get_terminal_size((80, 20))
	for i in range(0, variables.height):
		cursorTo(0, i, True)
		print(utils.build(' ', variables.width), end='')
		
