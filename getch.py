import sys, tty, termios

# http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

def getch2():
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		finalize()
	return ch

def finalize():
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
