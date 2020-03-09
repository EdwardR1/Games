def generateDeck():
  suits = ["♤", "♡", "♢", "♧"]
  values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  deck = []
  for suit in suits:
    for value in values:
      deck.append(value + suit)
  return deck

def getDeck():
  return generateDeck()

def getValue(card):
  value = card[0:-1]
  if(value == "A"):
    return 1
  elif(value == "J"):
    return 11
  elif(value == "Q"):
    return 12
  elif(value == "K"):
    return 13
  return int(value)

def getSuit(card):
  return card[-1]

def sort(hand):
  for i in range(len(hand)):
    for j in range(i, len(hand)):
      if(getValue(hand[i]) < getValue(hand[j])):
        hand[i], hand[j] = hand[j], hand[i]

def isFlush(hand):
  for i in range(len(hand) - 1):
    if(getSuit(hand[i]) != getSuit(hand[i + 1])):
      return False
  return True

def isStraight(hand):
  for i in range(len(hand) - 1):
    if(getValue(hand[i]) - 1 != getValue(hand[i + 1])):
      return False
  return True

def hasThreeOfKind(hand):
  count = 0
  for i in range(len(hand) - 1):
    if(getValue(hand[i]) == getValue(hand[i + 1])):
      count += 1
  if(count == 2):
    return True
  return False

def hasTwoOfKind(hand):
  count = 0
  for i in range(len(hand) - 1):
    if(getValue(hand[i]) == getValue(hand[i + 1])):
      count += 1
  if(count == 1):
    return True
  return False

def hasFullHouse(hand):
  if(getValue(hand[2]) == getValue(hand[3])):
    if((getValue(hand[0]) == getValue(hand[1])) and (getValue(hand[2]) == getValue(hand[3]) and (getValue(hand[3]) == getValue(hand[4])))):
      return True
  else:
    if((getValue(hand[0]) == getValue(hand[1]) and getValue(hand[1]) == getValue(hand[2])) and (getValue(hand[3]) == getValue(hand[4]))):
      return True
  return False


def hasFourOfKind(hand):
  count = 0
  for i in range(len(hand) - 1):
    if(getValue(hand[i]) == getValue(hand[i + 1])):
      count += 1
  if(count == 3):
    return True
  return False

def isStraightFlush(hand):
  return isStraight(hand) and isFlush(hand)


def printHandType(hands, name):
  print(f"Hand: {name} Hand", hands[name])

def main():
  deck = getDeck()
  hands = {
  "Two":[deck[0], deck[13], deck[27], deck[12], deck[10]],
   "Three": [deck[0], deck[13], deck[26], deck[12], deck[10]],
   "Flush": [deck[0], deck[1], deck[2], deck[3], deck[4]],
   "FullHouse": [deck[0], deck[13], deck[1], deck[14], deck[27]],
   "Four": [deck[0], deck[13], deck[26], deck[39], deck[1]],
   "StraightFlush": [deck[0], deck[1], deck[2], deck[3], deck[4]]
   }

  for hand in hands:
    sort(hands[hand])

  print("Deck:",deck)

  printHandType(hands, "Two")
  printHandType(hands, "Three")
  printHandType(hands, "Flush")
  printHandType(hands, "FullHouse")
  printHandType(hands, "Four")
  printHandType(hands, "StraightFlush")


  print("isFlush:", isFlush(hands["Flush"]))
  print("hasThreeOfKind:", hasThreeOfKind(hands["Three"]))
  print("hasTwoOfKind:", hasTwoOfKind(hands["Two"]))
  print("hasFullHouse:", hasFullHouse(hands["FullHouse"]))
  print("hasFourOfKind:", hasFourOfKind(hands["Four"]))
  print("isStraightFlush:", isStraightFlush(hands["StraightFlush"]))

main()

