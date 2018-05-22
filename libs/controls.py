from libs import getch
import queue
import threading
import os

def getInputBuffer():
	inputBuffer = ""
	while not queue.empty():
		inputBuffer += queue.get()
	return inputBuffer
	
	
def startWorker():
	worker.start()
	
def finalize():
	getch.finalize()
	
def worker():
	while threading.main_thread().is_alive():
		ch = getch.getch2()
		if ch is not "":
			queue.put(ch, True, None)
	if not threading.main_thread().is_alive():
		os.system('setterm -cursor on')
		getch.finalize()
			
queue = queue.LifoQueue()

worker = threading.Thread(target=worker)
