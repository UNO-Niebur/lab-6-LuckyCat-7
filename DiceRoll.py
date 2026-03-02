#DiceRoll.py
#Name: Tori Gregory
#Date:3/1/26
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 =random.randint(1,6)
    rolls[(dice1 - 1) + (dice2)] = rolls[(dice1 - 1) + (dice2)] + 1

  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 1
  for  count in rolls:
    print(dice, " : ", count)
    dice = dice + 1
    totalrolls = sum(rolls)
    percentage = count / totalrolls * 100
    print(percentage, "%")
if __name__ == '__main__':
  main()
