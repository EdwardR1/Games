# Work in progress still!

from random import randint

def assembleDeck():
  colors = ['B', 'G', 'Y', 'R']
  values = [str(f) for f in range(1, 10)]
  specials = ['SKIP', "+2", 'REWIND']
  uniqueCards = ["+4_", "Pick_"]
  regularCards = [value + color for color in colors for value in values]
  specialCards = [special + color for color in colors for special in specials]
  deck = 4 * uniqueCards + specialCards + regularCards
  return deck

def getColor(card):
  color = card[-1]
  if(color == "_"):
    return "Wild"
  elif(color == "B"):
    return "Blue"
  elif(color == "R"):
    return "Red"
  elif(color == "Y"):
    return "Yellow"
  elif(color == "G"):
    return "Green"

def getCardValue(card):
  if(len(card) == 2):
    return card[0]
  else:
    return "Wild"

def isWild(card):
  return getCardValue(card) == "Wild"

def draw(deck):
  i = randint(0, len(deck) - 1)
  card = deck[i]
  deck.pop(i)
  return card

def draw4(playerHand, deck):
  for _ in range(4):
    playerHand.append(draw(deck))

def getNumberOfPlayers():
  try:
    num = int(input("Please input a number of players: "))
    if(num < 0):
      raise ValueError
    return num
  except ValueError:
    print("Invalid input!")
    return getNumberOfPlayers()

def setPlayerDetails(numberOfPlayers):
  players = {}
  for n in numberOfPlayers:
    name = input(f"Please input the name of Player {n + 1}: ")
    players[name] = {"Name": name, "Hand": []}
  return players


def cardCanBePlayed(currentCard, attemptedCard):
  if(getCardValue(attemptedCard) == "Wild" or getColor(attemptedCard) == "Wild"):
    return True
  elif(getCardValue(currentCard) == getCardValue(attemptedCard)):
    return True
  elif(getColor(currentCard) == getColor(attemptedCard)):
    return True
  return False

def playCard(card, playerHand, nextPlayerHand, field):
  for (i, c) in enumerate(playerHand):
    if(c == card):
      playerHand.pop(i)
      break
  return card

def debug():
  deck = assembleDeck()
  print(deck)

# debug()


def main():
  DEFAULT_NUM_OF_CARDS = 5
  deck = assembleDeck()
  players = setPlayerDetails(getNumberOfPlayers())
  for _ in range(DEFAULT_NUM_OF_CARDS):
    for name in players:
      players[name]["Hand"].append(draw(deck))