import drawing
import variables
import utils
import controls
import engine
import os

def main():
	drawing.clearAll()
	drawing.buildFrame()
	controls.startWorker()
	gameLoop()

def gameLoop():
	global pos_x, pos_y, size, ticks
	os.system('setterm -cursor off')
	while True:
		inputBuffer = controls.getInputBuffer()
		print(inputBuffer, end='')
		handleInputs(inputBuffer)
		if variables.pos_x > variables.width:
			variables.pos_x = 0
		drawing.draw()
		utils.WaitNextTick(variables.ticks)
		

def handleInputs(inputs):
	for char in inputs:
		if char is 'x':
			utils.exit()
		if char is 'a':
			engine.handleLeft()
		if char is 'd':
			engine.handleRight()

main()
