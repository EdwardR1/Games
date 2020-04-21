from random import randint

def getLimit():
  try:
    val = int(input("Please input an upper limit for the computer to pick from: "))
    if(val < 1):
      raise ValueError
    return val
  except ValueError:
    print("Invalid input! Try again!")
    return getLimit()
  
def getUserGuess():
  try:
    guess = int(input("Please input a number: "))
    if(guess < 1):
      raise ValueError
    return guess
  except ValueError:
    print("Invalid input! Try again!")
    return getUserGuess()
  

def appendToFile(limit, value, guesses, filename="counts.txt"):
  with open(filename, "a") as f:
    f.write(str(limit))
    f.write(":")
    f.write(str(value))
    f.write(":")
    f.write(str(guesses))
    f.write(",\n")

def interactive():
  counter = 1
  limit = getLimit()
  value = randint(1, limit)
  user = getUserGuess()
  while(user != value):
    if(user > value):
      print("Your number is greater than the computer chosen value")
    else:
      print("Your number is less than the computer chosen value")
    counter += 1
    user = getUserGuess()
  print("Well done! You solved it in", counter, "times!")
  appendToFile(limit, value, counter, "counts.txt")

interactive()


def binarySearch(value, low, high, counter = 1):
  mid = int((low + high) / 2)
  if(mid == value):
    return counter
  elif(mid > value):
    return binarySearch(value, low, mid - 1, counter + 1)
  else:
    return binarySearch(value, mid + 1, high, counter + 1)


def automated(limit):
  value = randint(1, limit)
  comp = int(limit / 2)
  counter = binarySearch(value, 1, limit)
  appendToFile(limit, value, counter, "automated_counts.txt")

# automated()

def automated_main():
  limits = [f for f in range(50, 10001, 50)]
  for lim in limits:
    automated(lim)
# 
# automated_main()