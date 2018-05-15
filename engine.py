import variables

def handleLeft():
	variables.pos_x -= 1
	if variables.pos_x < 0:
		variables.pos_x = variables.width - 1

def handleRight():
	variables.pos_x += 1
	if variables.pos_x >= variables.width:
		variables.pos_x = 0
