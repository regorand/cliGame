import time
import controls
import sys
import drawing

def build(char, amount):
	res = ''
	if amount > 0:
		for i in range(0, amount):
			res += char	
	return res


def getWaitDelay(ticksPerSec):
	return 1000/ticksPerSec

def WaitNextTick(ticksPerSec):
	sleepMs(1000/ticksPerSec)

def sleepMs(ms):
	time.sleep(ms/1000)

def doPrint(msg):
	print(msg, end='')
	
def exit():
	drawing.clearAll()
	drawing.cursorTo(0, 0, False)
	controls.finalize()
	sys.exit(0)
