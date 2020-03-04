board = []
players = {1: {"Name": "", "Marker": ""}, 2: {"Name":"", "Marker":""}}

def createBoard():
	global board
	for i in range(3):
		board.append([])
		for j in range(3):
			board[i].append("-")
	
def setPlayerName(playerNumber, name):
	global players
	players[playerNumber]["Name"] = name

def setPlayerMarker(playerNumber, marker):
	global players
	players[playerNumber]["Marker"] = marker

def isAvailable(x, y):
	if(x > 3 or y > 3):
		print("Invalid values!")
		return False
	return board[x][y] == '-'

def draw(x, y, marker):
	if(isAvailable(x, y)):
		board[x][y] = marker
		return 0
	else:
		print("Cannot place a marker there!")
		return 1

def getPositions():
	try:
		x = int(input("Please input an x coordinate: "))
		y = int(input("Please input a y coordinate: "))
		return (x,y)
	except ValueError:
		print("Invalid positions!")


def hasVerticalWin(players):
	marker1 = players[1]["Marker"]
	marker2 = players[2]["Marker"]
	for i in range(len(board)):
		if(board[0][i] == marker1 and board[1][i] == marker1 and board[2][i] == marker1):
			return 1
		elif(board[0][i] == marker2 and board[1][i] == marker2 and board[2][i] == marker2):
			return 2
	return False

def hasHorizontalWin(players):
	marker1 = players[1]["Marker"]
	marker2 = players[2]["Marker"]
	for i in range(len(board)):
		if(board[i][0] == marker1 and board[i][1] == marker1 and board[i][2] == marker1):
			return 1
		elif(board[i][0] == marker2 and board[i][1] == marker2 and board[i][2] == marker2):
			return 2
	return False

def hasDiagonalWin(players):
	marker1 = players[1]["Marker"]
	marker2 = players[2]["Marker"]
	if(board[0][0] == marker1 and board[1][1] == marker1 and board[2][2] == marker1):
		return 1
	elif(board[0][2] == marker1 and board[1][1] == marker1 and board[2][0] == marker1):
		return 1
	elif(board[0][0] == marker2 and board[1][1] == marker2 and board[2][2] == marker2):
		return 2
	elif(board[0][2] == marker2 and board[1][1] == marker2 and board[2][0] == marker2):
		return 2
	return False
	
def canStillPlay():
	for i in range(3):
		for j in range(3):
			if(board[i][j] == "-"):
				return True
	return False

def stillPlaying():
	if(hasDiagonalWin(players) == False and  hasVerticalWin(players) == False and hasHorizontalWin(players) == False and canStillPlay()):
		return True
	return False



def printBoard():
	print("Board: ")
	for i in range(3):
		for j in range(3):
			print(board[i][j], end=" ")
		print()

def main():
	createBoard()
	player1name = input("Please input the first player's name: ")
	setPlayerName(1, player1name)
	player1Marker = input("Please input a character to serve as the marker for the first player: ")
	setPlayerMarker(1, player1Marker)

	print("Thank you! Now, for player 2's details!")
	player2Name = input("Please input the second player's name: ")
	setPlayerName(2, player2Name)
	player2Marker = input("Please input a character to serve as the marker for the second player: ")
	setPlayerMarker(2, player2Marker)

	print("Let's begin!")

	while(stillPlaying()):
		print("Player 1 Move: ")
		pos = getPositions()
		if(not isAvailable(pos[0], pos[1])):
			print("Invalid location")
			pos = getPositions()
		draw(pos[0], pos[1], players[1]["Marker"])
		printBoard()
		if(not stillPlaying()):
			break
		print("Player 2 Move: ")
		pos = getPositions()
		if(not isAvailable(pos[0], pos[1])):
			print("Invalid location")
			pos = getPositions()
		draw(pos[0], pos[1], players[2]["Marker"])
		printBoard()
	
main()