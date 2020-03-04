board = []
def initializeBoard():
  for i in range(8):
    board.append([])
    for _ in range(8):
      board[i].append("-")

def movePawn(currentX, currentY, isOpen = False):
  # forward 2 if opening, 1 otherwise
  if(isOpen):
    return (currentX, currentY - 2)
  return (currentX, currentY - 1)

def moveKnights(currentX, currentY, newX, newY):
  # forward L
  pass

def moveBishop(currentX, currentY, newX, newY):
  # diagonal
  pass

def moveRook(x, y, newX, newY):
  # forward, backward, left, right
  pass

def moveQueen(currentX, currentY, newX, newY):
  # move all directions
  pass

def moveKing(currentX, currentY, newX, newY):
  # move one any direction
  pass

def convertFromChessNotation(letter, number):
  letter = letter.lower()
  col = 0
  if(letter == "a"):
    col = 0
  elif(letter == 'b'):
    col = 1
  elif(letter == 'c'):
    col = 2
  elif(letter == "d"):
    col = 3
  elif(letter == 'e'):
    col = 4
  elif(letter == 'f'):
    col = 5
  elif(letter == "g"):
    col = 6
  elif(letter == 'h'):
    col = 7
  row = abs(number - 8)
  return (row, col)

def initializePieces():
  pieces = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'Kn', 'Kn', 'B', 'B', 'R', 'R', 'Q', 'Ki']  
  whitePieces = ["W" + piece for piece in pieces]
  blackPieces = ["B" + piece for piece in pieces]
  totalPieces = {"White": whitePieces, "Black": blackPieces}
  return totalPieces

def main():
  # initializePieces()
  print(convertFromChessNotation("h", 1))

main()