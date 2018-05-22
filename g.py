#!/usr/bin/python3
from engine import gamestate
from engine import engine
from libs import drawing
from libs import variables
from libs import utils
from libs import controls
import os

gameState = gamestate.Gamestate()

def main():
	drawing.clearAll()
	drawing.buildFrame()
	controls.startWorker()
	gameLoop()

def gameSetup():
	gamestate.createGameState()

def gameLoop():
	os.system('setterm -cursor off')
	while True:
		engine.doTick(gameState)
		inputBuffer = controls.getInputBuffer()
		print(inputBuffer, end='')
		handleInputs(inputBuffer)
		if variables.pos_x > variables.width:
			variables.pos_x = 0
		drawing.draw(gameState)
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
				engine.handleLeft(gameState)
			if char is 'd':
				cmdsThisTick.append('d')
				engine.handleRight(gameState)
			if char is 'w':
				cmdsThisTick.append('w')
				engine.handleJump(gameState)

main()
