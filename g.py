import drawing
import variables
import utils
import controls
import engine
import os

player = {
'pos_x': 1,
'pos_y': 0,
'isInAir': False,
'remainingAirTime': 0
}

def main():
	drawing.clearAll()
	drawing.buildFrame()
	controls.startWorker()
	gameLoop()

def gameLoop():
	global pos_x, pos_y, size, ticks
	os.system('setterm -cursor off')
	while True:
		engine.doTick(player)
		inputBuffer = controls.getInputBuffer()
		print(inputBuffer, end='')
		handleInputs(inputBuffer)
		if variables.pos_x > variables.width:
			variables.pos_x = 0
		drawing.draw(player)
		utils.WaitNextTick(variables.ticks)
		

def handleInputs(inputs):
	cmdsThisTick = []
	for char in inputs:
		if not char in cmdsThisTick:
			if char is 'x':
				cmdsThisTick.append('x')
				utils.exit()
			if char is 'a':
				cmdsThisTick.append('a')
				engine.handleLeft(player)
			if char is 'd':
				cmdsThisTick.append('d')
				engine.handleRight(player)
			if char is 'w':
				cmdsThisTick.append('w')
				engine.handleJump(player)

main()
