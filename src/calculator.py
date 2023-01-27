from addition import additionMode
from typing import clearScreen, typingInput, typingPrint

import os
import sys
import time

PIE = 3.14159265359

#-----------------------------------------------------------------
def printMenu():
  typingPrint('--------------\n')
  typingPrint('Menu\n')
  typingPrint('--------------')
  print(' ')
  print('1.Addition\n2.Subtraction\n3.Multiplcation\n4.Divsion\n5.Squared\n6.Pythagorean Theorem \n7.Square Root\n8.Area of a Circle\n9.Powered\n10.Percentage\n------Quit------\n------Help------')

#-----------------------------------------------------------------
def SubtractionMode():
  while True:
    num1=input('Enter a number:   ' )
    if num1 == 'back' :
      return
    num2=input('Enter a number:   ' )
    real_answer = float(num1) - float(num2)
    print(' ')
    time.sleep(1)
    print('%s - %s = %s ' % (num1, num2, real_answer))
#-----------------------------------------------------------------

clearScreen()
typingPrint('Welcome User\n')
time.sleep(1.5)
Val = True
while Val:  

  printMenu()
  print(' ')
  act = typingInput('Chose an action above:  ')
  print(' ')
  if act == '1':
    clearScreen()
    additionMode()
  if act == '2' :
    SubtractionMode()
  if act == '3' :
    MultiplcationMode()
  if act == '4' :
    DivsionMode()
  if act == '5' :
    SquareMode()
  if act == '6' :
    PythagoreanMode()
  if act == '7' :
    SquareRootMode()
  if act == '8' :
    circleMode()
  if act == '9' :
    Powered()
  if act == '10' :
    percent()
  if act == 'help' or act == 'Help' :
    Help()
  if act == 'quit' or act == 'stop' :
    clearScreen()
    Val = False
  