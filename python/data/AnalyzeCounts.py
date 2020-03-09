from math import log
def parseData(file = "counts.txt"):
  data = {}
  with open(file, "r") as f:
    for line in f:
      line = line.strip().strip(",")
      values = line.split(":")
      try:
        limit = int(values[0])
        value = int(values[1])
        guesses = int(values[2])
        if(limit not in data):
          data[limit] = [{value: guesses}]
        else:
          data[limit].append({value: guesses})
      except ValueError:
        continue
  # print(data)
  return data

def calculateAverages(data):
  averages = {}
  for limit in data:
    if(limit not in averages):
      averages[limit] = 0
    for inner in data[limit]:
      for key in inner:
        averages[limit] += inner[key]
    averages[limit] /= len(data[limit])
  return averages

def printAverages(averages):
  for limit in averages:
    print(f"{limit}: {averages[limit]:.1f}")

def sortAverages(averages):
  keys = list(averages.keys())
  for i in range(len(keys)):
    for j in range(i, len(keys)):
      if(keys[i] > keys[j]):
        keys[i],keys[j] = keys[j],keys[i]
  sorted = {}
  for key in keys:
    sorted[key] = averages[key]
  averages = sorted
  return averages
  

def calculateMathematicalAverages(averages):
  keys = list(averages.keys())
  values = list(averages.values())
  expected = {}
  actual = averages
  for key in keys:
    expected[key] = log(key, 2)
  return expected

def compareWithMathematicalAverages(averages):
  keys = list(averages.keys())
  values = list(averages.values())
  expected = calculateMathematicalAverages(averages)
  
  print("Limit : Expected : Actual")
  for key in expected:
    print(f"{key} : {expected[key]:.1f} : {averages[key]:.1f}")


def writeToStatsFile(averages, filename = 'stats.txt'):
  with open(filename, "w") as f:
    f.write("Limit\t:\tExpected\t:\tActual\n")
    expected = calculateMathematicalAverages(averages)
    for key in expected:
      f.write(f"{key}\t:\t{expected[key]:.1f}\t:\t{averages[key]:.1f}\n")
    

def main():
  data = parseData()
  averages = calculateAverages(data)
  averages = sortAverages(averages)
  # printAverages(averages)

  compareWithMathematicalAverages(averages)

  writeToStatsFile(averages)

main()

def automated():
  data = parseData("automated_counts.txt")
  averages = calculateAverages(data)
  averages = sortAverages(averages)
  compareWithMathematicalAverages(averages)
  writeToStatsFile(averages, "automated_stats.txt")

# automated()