#WordIndex.py
#Name:Tori Gregory
#Date:3/1/26
#Assignment: Lab 6

def main():
  lineNum = 0
  words = {}
  decidetext = input("What text would you like: (gettysberg or fish)" )
  if decidetext == "fish":
    textFile = open("fish.txt", 'r')
    for line in textFile:
      lineNum = lineNum + 1
      wordList = line.split()
      for w in wordList:
        w = w.lower()
        w = w.replace(",", "")
        w = w.replace(".", "")
        w = w.replace("!", "")
        if w in words:
         if lineNum not in words[w]:
          words[w].append(lineNum)
        else:
          words[w] = [lineNum]
        for word in words:
          print(word, words[word])
      print(line)
  elif decidetext == "gettysberg":
    textFile = open("gettysberg.txt", 'r')
    for line in textFile:
      lineNum = lineNum + 1
      wordList = line.split()
      for w in wordList:
        w = w.lower()
        w = w.replace(",", "")
        w = w.replace(".", "")
        w = w.replace("!", "")
        if w in words:
         if lineNum not in words[w]:
            words[w].append(lineNum)
        else:
            words[w] = [lineNum]
        for word in words:
          print(word, words[word])
    print(line)
  else:
    print("No valid file found")

   #create an empty dictionary
  


if __name__ == '__main__':
  main()
