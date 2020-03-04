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


def check(char, actualArray):
    for i in range(len(actualArray)):
        if(actualArray[i] == char):
            return i
    return -1


def addFailed(char, failed):
    failed.append(char)


def setChar(char, actual, hidden, failed):
    index = check(char, actual)
    if(index == -1):
        addFailed(char, failed)
        return
    hidden[index] = char


def main():
    OPPORTUNITIES = 10
    failed = []
    words = parseWords()
    print("Number of available words:", len(words))
    # word = getRandomWord(words)
    word = "Hello"
    actual = toCharArray(word)
    hidden = toHiddenWord(word)
    # while(len(failed) < OPPORTUNITIES):
    setChar("a", actual, hidden, failed)
    print("Actual:", actual)
    print("Hidden:", hidden)
    print("Failed:", failed)


main()
