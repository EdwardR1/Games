from random import choice


def parseWords():
    filename = "words.csv"
    words = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip().strip(",")
            words.append(line)
    return words


def getRandomWord(words):
    if(len(words) == 0):
        return "default"
    return choice(words)


def toCharArray(word):
    chars = []
    for chr in word:
        chars.append(chr.lower())
    return chars


def toHiddenWord(word):
    hiddenChars = toCharArray(word)
    for i in range(len(hiddenChars)):
        if(hiddenChars[i].isalpha()):
            hiddenChars[i] = "*"
    return hiddenChars


def compareStrings(actual, hidden):
  return actual == hidden

def check(char, actualArray):
    return char in actualArray 


def addFailed(char, failed):
    failed.append(char)

def setChar(char, actual, hidden, failed):
    if(not check(char, actual)):
      addFailed(char, failed)
    else:
      for (i, chr) in enumerate(actual):
        if(chr == char):
          hidden[i] = char

def toString(charArray):
    return "".join(charArray)

def main():
    tries = 0
    OPPORTUNITIES = 10
    word = getRandomWord(parseWords)
    failed = []
    actual = toCharArray(word)
    hidden = toHiddenWord(word)
    while(len(set(failed)) < OPPORTUNITIES):
        char = input("Please input a character to try: ")
        setChar(char, actual, hidden, failed)
        tries += 1
        print("Word: ", hidden)
        if(compareStrings(actual, hidden)):
          print("You got it in", tries)
          print("You missed", len(failed), "letters!")
          break
    print("Your word was:", toString(actual))
    if(len(set(failed)) >= OPPORTUNITIES):
      print("You didn't get your word in", OPPORTUNITIES, "tries!")
    
main()


