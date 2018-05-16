import variables

def handleLeft():
	variables.pos_x -= 1
	if variables.pos_x < 1:
		variables.pos_x = variables.width

def handleRight():
	variables.pos_x += 1
	if variables.pos_x >= variables.width:
		variables.pos_x = 1
