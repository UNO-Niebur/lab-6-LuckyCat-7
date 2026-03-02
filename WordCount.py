#WordCount.py
#Name:Tori Gregory
#Date:3/1/26
#Assignment: Lab 6

def main():
  decidetext = input("Choose text(gettysberg or fish):" )
  if decidetext == "gettysberg":
    textFile = open("gettysberg.txt", 'r')
    wordCount = 0
    letterCount = 0
    lineCount = 0
    for line in textFile:
      print(line)
      lineCount = lineCount + 1
      words = line.split()
    for w in words:
      wordCount = wordCount + 1
    for len in line:
      letterCount = letterCount + 1
    print("Lines:", lineCount, "Letters:", letterCount, "Words:", wordCount)
  elif decidetext == "fish":
    textFile = open("fish.txt", 'r')
  wordCount = 0
  letterCount = 0
  lineCount = 0
  for line in textFile:
    print(line)
    lineCount = lineCount + 1
    words = line.split()
  for w in words:
    wordCount = wordCount + 1
  for len in line:
    letterCount = letterCount + 1
  print("Lines:", lineCount, "Letters:", letterCount, "Words:", wordCount)
  

if __name__ == '__main__':
  main()
