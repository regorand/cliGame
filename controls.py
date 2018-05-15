import getch as getch
import queue
import threading

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
	while True:
		ch = getch.getch2()
		if ch is not "":
			queue.put(ch, True, None)
			
queue = queue.LifoQueue()

worker = threading.Thread(target=worker)
worker.daemon = True
