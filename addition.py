import os
import sys
import time

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def clearScreen():
  os.system("cls")

def additionMode():
  while True:  
    print("Mode: Addition")
    print(" ")
    num1 = typingInput('Enter a number: ' )
    if num1 == 'back':
      clearScreen()
      return
    num2= typingInput('Enter a number: ' )
    if num2 == 'back':
      return
    real_answer = float(num1) + float(num2)
    print(' ')
    time.sleep(1)
    print('%s + %s = %s' % (num1, num2, real_answer))
    time.sleep(2)
    clearScreen()