from random import randint

def generateDeck():
	suits = ["♤", "♡", "♢", "♧"]
	values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	deck = []
	for suit in suits:
		for value in values:
			deck.append(value + suit)
	return deck

def parseCard(card):
	value = card[0:-1]
	if(value == "A"):
		return 11
	elif(value == "J" or value == "Q" or value == "K"):
		return 10
	return int(value)

def inputInt(purpose, low, high=-1):
	try:
		print(purpose)
		if(high != -1):
			val = int(input(f"Please input a number between {low} and {high}: "))
			if(val < low or val > high):
				print("Out of boundaries!")
				return inputInt(purpose, low, high)
		else: 
			val = int(input(f"Please input a number greater than {low}: "))
			if(val < low):
				print("Out of boundaries!")
				return inputInt(purpose, low, high)
		return val
	except ValueError:
		print("Input not an integer! Try again!")
		return inputInt(purpose, low, high)


def getNumberOfPlayers():
	num = inputInt("How many players?", 2)
	return num

def initialisePlayers(numberOfPlayers):
	players = {}
	for i in range(numberOfPlayers):
		name = input("Please input a name: ")
		while(name in players):
			print("Name already chosen! Please pick another name! ")
			name = input("Please input a name: ")
		players[name] = {}
		players[name]["Name"] = name
		players[name]["Stay"] = False
		players[name]["Bust"] = False
		players[name]["Hand"] = []
	return players

def getNextPlayer(currentPlayer, players):
	playerNames = list(players.keys())
	currIndex = -1
	nextIndex = -1
	for i in range(len(playerNames)):
		if(playerNames[i] == currentPlayer["Name"]):
			currIndex = i
			break
	if(currIndex == len(players) - 1):
		nextIndex = 0
	else:
		nextIndex = currIndex + 1
	while(players[playerNames[nextIndex]]["Stay"] or players[playerNames[nextIndex]]["Bust"]):
		if(allStayed(players)):
			break
		if(not stillPlaying(players)):
			break
		if(nextIndex != len(players) - 1):
			nextIndex += 1
		else:
			nextIndex = 0
	return players[playerNames[nextIndex]]
	
def printHands(players):
	for name in players:
		print(name, players[name]["Hand"])
		
def getWinner(players):
	playersNotBusted = []
	playerHandSums = {}
	for player in players:
		if(not players[player]["Bust"]):
			playersNotBusted.append(players[player])
	for player in playersNotBusted:
		playerHandSums[player["Name"]] = getPlayerHandValue(player)
	maxNonBustHand = max(playerHandSums.values())
	for playerName in playerHandSums.keys():
		if(playerHandSums[playerName] == maxNonBustHand):
			return players[playerName]
	# pass

def allStayed(players):
	for player in players:
		if(not players[player]["Stay"]):
			return False
	return True

def stillPlaying(players):
	stayQuantity = 0
	bustQuantity = 0
	for player in players:
		if(players[player]["Stay"]):
			stayQuantity += 1
	for player in players:
		bust(players[player])
		if(players[player]["Bust"]):
			bustQuantity += 1
	if(allStayed(players)):
		return False
	elif(bustQuantity == len(players) - 1):
		return False
	elif(stayQuantity + bustQuantity == len(players)):
		return False
	return True

def deal(player, deck):
	index = randint(0, len(deck) - 1)
	player["Hand"].append(deck[index])
	deck.pop(index)

def stay(player):
	player["Stay"] = True

def getPlayerHandValue(player):
	total = 0
	for card in player["Hand"]:
		total += parseCard(card)
	return total

def bust(player):
	if(getPlayerHandValue(player) > 21):
		player["Bust"] = True

def getChoice(player):
	MIN = 1
	MAX = 2

	choice = input(f"{player['Name']}: [1] to Hit, [2] to Stay: ")
	try:
		value = int(choice)
		if(value < MIN or value > MAX):
			raise ValueError
		return value
	except ValueError:
		print("Invalid value! Try Again!")
		return getChoice(player)

def play(players):
	deck = generateDeck()
	currentPlayer = players[list(players.keys())[0]]
	for _ in range(len(players) * 2):
		deal(currentPlayer, deck)
		currentPlayer = getNextPlayer(currentPlayer, players)
	printHands(players)
	print()
	while(stillPlaying(players)):
		choice = getChoice(currentPlayer)
		if(choice == 1):
			deal(currentPlayer, deck)
		else:
			stay(currentPlayer)
		print()
		printHands(players)

		currentPlayer = getNextPlayer(currentPlayer, players)
	winner = getWinner(players)

	print(f"Winner is: {winner['Name']} with a score of {getPlayerHandValue(winner)}")
	print()


def production():
	players = initialisePlayers(getNumberOfPlayers())
	play(players)


def debug():
	players = {
		'Edward': {'Name': 'Edward', 'Stay': False, 'Hand': [], 'Bust': False}, 'John': {'Name': 'John', 'Stay': False, 'Hand': [], 'Bust': False}, 
		'Yadan': {'Name': 'Yadan', 'Stay': False, 'Hand': [], 'Bust': False}
		}
	play(players)

production()