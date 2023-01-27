from addition import additionMode
from subtraction import subtractionMode
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

clearScreen()
typingPrint('Welcome User\n')
print(' ')
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
  if act == '2':
    clearScreen()
    subtractionMode()
  if act == 'stop':
    Val = False