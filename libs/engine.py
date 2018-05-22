from libs import variables

def handleLeft(player):
	player['pos_x'] -= 1
	if player['pos_x'] < 1:
		player['pos_x'] = variables.width

def handleRight(player):
	player['pos_x'] += 1
	if player['pos_x'] >= variables.width:
		player['pos_x'] = 1
		
def handleJump(player):
	player['pos_y'] += 1
	player['remainingAirTime'] = int(variables.ticks / variables.airtimeFactor)
	player['isInAir'] = True
	
def doTick(player):
	if player['isInAir']:
		if player['remainingAirTime'] == 0:
			if player['pos_y'] > 0:
				player['pos_y'] -= 1
				if player['pos_y'] == 0:
					player['isInAir'] = False
				else:
					player['remainingAirTime'] = int(variables.ticks / variables.airtimeFactor)
					
		else:
			player['remainingAirTime'] -= 1
